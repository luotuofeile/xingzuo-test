// 本地渲染校验 month.html（用 managed workspace 的 playwright）
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const fileUrl = 'file:///' + path.resolve(__dirname, 'yunshi', 'month.html').replace(/\\/g, '/');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 420, height: 900 } });
  await page.goto(fileUrl, { waitUntil: 'load' });

  const title = await page.title();
  const navCount = await page.locator('nav a').count();
  const sectionCount = await page.locator('section[id]').count();
  const hasMonthNote = (await page.locator('.month-note').count()) > 0;
  const firstSign = await page.locator('section[id] h3').first().textContent();

  console.log('标题:', title);
  console.log('导航链接数:', navCount);
  console.log('星座 section 数:', sectionCount);
  console.log('月运说明条:', hasMonthNote);
  console.log('第一个星座:', firstSign);

  await page.screenshot({ path: path.join(__dirname, 'month_preview.png'), fullPage: false });
  // 再截一张滚动到金牛的（验证锚点跳转）
  await page.goto(fileUrl + '#jinniu', { waitUntil: 'load' });
  await page.screenshot({ path: path.join(__dirname, 'month_preview_jinniu.png') });

  await browser.close();
  console.log('截图完成');
})().catch(e => { console.error(e); process.exit(1); });