#!/bin/bash
set -e  # Stop script on error

echo "Installing dependencies..."
yarn install --frozen-lockfile  # or npm install

echo "Building the project..."
yarn build  # or npm run build

echo "Starting the app..."
yarn start  # or npm start
