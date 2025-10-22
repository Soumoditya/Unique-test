#!/bin/bash
REPO_DIR="/path/to/kolkata-cctv-stream"  # Replace with your repo path
cd $REPO_DIR
git pull
cp -r docs/* .  # Copy stream files to repo root for GitHub Pages
git add .
git commit -m "Update live stream - fuck yeah $(date)"
git push origin main
echo "Pushed to GitHub, you glorious bastard!"
