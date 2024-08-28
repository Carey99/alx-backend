import express from 'express';
import { createClient } from 'redis';
import { listProducts, getItemById } from './data.js';
import { promisify } from 'util';

const app = express();
const port = 1245;

const client = createClient();
const reserveStockByIdAsync = promisify(client.set).bind(client);
const getCurrentReservedStockByIdAsync = promisify(client.get).bind(client);

client.on('error', (err) => {
  console.error(`Redis error: ${err.message}`);
});

app.get('/list_products', (req, res) => {
  const products = listProducts.map(product => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const id = parseInt(itemId, 10);
  const product = getItemById(id);
  
  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  
  const reservedStock = await getCurrentReservedStockByIdAsync(`item.${id}`);
  const currentQuantity = product.stock - (parseInt(reservedStock, 10) || 0);
  
  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: currentQuantity,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const id = parseInt(itemId, 10);
  const product = getItemById(id);
  
  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  
  const reservedStock = await getCurrentReservedStockByIdAsync(`item.${id}`);
  const currentQuantity = product.stock - (parseInt(reservedStock, 10) || 0);
  
  if (currentQuantity < 1) {
    return res.json({ status: 'Not enough stock available', itemId: id });
  }
  
  await reserveStockByIdAsync(`item.${id}`, (parseInt(reservedStock, 10) || 0) + 1);
  
  res.json({ status: 'Reservation confirmed', itemId: id });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
