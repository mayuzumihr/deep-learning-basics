// server.mjs
import https from 'https';
import fs from 'fs';
import express from 'express';
import { createProxyMiddleware } from 'http-proxy-middleware';

const app = express();

const sslOptions = {
    key: fs.readFileSync('./privkey.pem'),
    cert: fs.readFileSync('./cert.pem'),
    passphrase: 'Mayu1231!'    //Change to your passphrase
};

app.use('/', createProxyMiddleware({
    target: 'http://localhost:8000',
    changeOrigin: true,
    secure: false
}));

https.createServer(sslOptions, app).listen(3000, () => {
    console.log('HTTPS Proxy server is running on https://www.example.local:3000');
});