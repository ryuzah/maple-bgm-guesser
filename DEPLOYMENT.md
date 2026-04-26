# Maple BGM Guessing Game Deployment Guide

## 🚀 Quick Deployment Options

### Option 1: Netlify (Recommended - Free & Easy)
1. **Create Account**: Sign up at [netlify.com](https://netlify.com)
2. **Drag & Drop**: Drag your entire project folder to the deploy area
3. **Instant URL**: Get immediate HTTPS URL (e.g., `your-game.netlify.app`)
4. **Custom Domain**: Free custom domain support available

**Pros**: Free SSL, automatic deployments, custom domains, CDN
**Cons**: 100GB bandwidth/month limit

### Option 2: GitHub Pages (Free)
1. **Create Repository**: Create new GitHub repository
2. **Upload Files**: Push all files including `bgm_files/` folder
3. **Enable Pages**: Go to Settings → Pages → Source: Deploy from branch
4. **Deploy**: Select main branch and save

**Pros**: Completely free, Git integration, custom domains
**Cons**: 1GB storage limit, manual deployment process

### Option 3: Vercel (Free)
1. **Create Account**: Sign up at [vercel.com](https://vercel.com)
2. **Import Project**: Connect GitHub repository or upload files
3. **Deploy**: Automatic deployment with HTTPS URL

**Pros**: Great performance, analytics, preview deployments
**Cons**: Similar bandwidth limits to Netlify

### Option 4: Traditional Hosting
1. **Purchase Plan**: Bluehost, SiteGround, Hostinger, etc.
2. **Upload Files**: Use FTP or cPanel File Manager
3. **Configure Domain**: Set up domain and SSL certificate

## 📁 Required Files for Deployment

Your project needs these essential files:

```
maple-bgm-game/
├── index.html                 # Main game file (58KB)
├── songs_metadata.json        # Song database (111KB)
├── bgm_files/                 # Audio files folder
│   ├── Floral Life - Henesys.mp3
│   ├── Go Picnic - Henesys.mp3
│   ├── Nightmare - Perion.mp3
│   └── ... (521 audio files)
├── README.md                  # Documentation
└── DEPLOYMENT.md              # This file
```

**Optional files to exclude:**
- All `.py` files (development scripts)
- `songs_metadata_backup_*.json` (backup files)
- Test files and scripts

## 🎵 Audio Files Considerations

### File Size Impact
- **521 songs × ~3MB each = ~1.5GB total**
- **Free hosting limits**: Netlify (100GB/month), GitHub Pages (1GB total)

### Recommendations
1. **Start with subset**: Deploy with 50-100 popular songs first
2. **Compress audio**: Use 128kbps MP3 instead of higher quality
3. **Monitor usage**: Check bandwidth usage regularly

### Alternative: YouTube Integration
Your game already supports YouTube URLs - you could:
- Deploy without local audio files
- Game will fall back to YouTube playback
- Much smaller deployment size

## 🛠️ Step-by-Step Netlify Deployment

### 1. Prepare Your Files
```bash
# Create deployment folder
mkdir maple-bgm-deploy
cp index.html maple-bgm-deploy/
cp songs_metadata.json maple-bgm-deploy/
cp -r bgm_files maple-bgm-deploy/
```

### 2. Deploy to Netlify
1. Go to [netlify.com](https://netlify.com)
2. Sign up (free)
3. Drag `maple-bgm-deploy` folder to deploy area
4. Wait for deployment (2-5 minutes)
5. Get your URL: `random-name-123456.netlify.app`

### 3. Test Your Site
- Open the provided URL
- Test game functionality
- Verify audio playback
- Check mobile compatibility

## 🛠️ Step-by-Step GitHub Pages Deployment

### 1. Create Repository
```bash
git init
git add index.html songs_metadata.json bgm_files/
git commit -m "Initial Maple BGM game deployment"
git branch -M main
git remote add origin https://github.com/username/maple-bgm-game.git
git push -u origin main
```

### 2. Enable GitHub Pages
1. Go to repository Settings
2. Scroll to "Pages" section
3. Source: Deploy from branch
4. Branch: main, folder: /root
5. Click Save

### 3. Access Your Site
- URL: `https://username.github.io/maple-bgm-game`
- Takes 1-2 minutes to deploy initially

## 🔧 Configuration Options

### Custom Domain (Netlify)
1. Go to Site settings → Domain management
2. Add custom domain
3. Update DNS records (provided by Netlify)
4. Automatic SSL certificate

### Custom Domain (GitHub Pages)
1. Go to repository Settings → Pages
2. Add custom domain
3. Update DNS records with your provider
4. Automatic HTTPS available

## 📊 Performance Optimization

### Before Deployment
- **Compress images**: Use TinyPNG for any images
- **Minify HTML**: Use HTML minifier (optional)
- **Optimize audio**: 128kbps MP3 is sufficient

### After Deployment
- **Test loading speed**: Use PageSpeed Insights
- **Check mobile**: Test on various devices
- **Monitor bandwidth**: Check hosting dashboard

## ⚠️ Important Considerations

### Copyright & Legal
- MapleStory BGMs are copyrighted material
- Consider fair use for educational/fan purposes
- Commercial use likely requires permission

### Bandwidth Limits
- **Netlify**: 100GB/month free, then $20/100GB
- **GitHub Pages**: 100GB/month soft bandwidth limit
- **Vercel**: 100GB/month free tier

### Maintenance
- **Update songs**: Add new BGMs to `songs_metadata.json`
- **Backup data**: Keep copies of your JSON files
- **Monitor usage**: Check if you're approaching limits

## 🚀 Advanced Options

### CDN Integration
- Use CloudFlare for free CDN
- Improves global loading speeds
- Basic DDoS protection

### Database Backend
- Replace JSON with Firebase/Supabase
- Dynamic song updates
- User progress tracking

### Progressive Web App
- Add service worker for offline play
- App-like experience on mobile
- Installable on home screen

## 📞 Support & Troubleshooting

### Common Issues
- **Audio not playing**: Check file paths and formats
- **Slow loading**: Consider reducing audio file count
- **Mobile issues**: Test responsive design

### Getting Help
- Netlify: [support.netlify.com](https://support.netlify.com)
- GitHub: [docs.github.com/en/pages](https://docs.github.com/en/pages)
- Game-specific: Check browser console for errors

---

**🎮 Happy gaming! Your Maple BGM guessing game is ready to share with the world!**
