# fastText-classification

## fastText classification for Chinese news

### Dataset

  Chinese news extracted from websites including the categories with "办公"，"军事"，"政务"，"科技"，"财经"，"其他".<br>

  The dataset format is as below.<br>

 
   __label__0 , 一 工作 思路 深入 贯彻 落实 科学 发展观 构建 和谐 社会 按照 抓 生产 保 供给 抓统 筹促 协调 抓 改革 增 活力 的 总体 要求 坚持 标本兼治 着力 治本 打 防 结合 综合治理 和 属地 管理 原则 以 规范 农资 市场 秩序 和 企业 生产 经营 行为 为 主线 以 源头 治理 大要案 查处 和 基层 农资 监管 能力 建设 为 重点 打击 假劣 促 生产 严查 违禁 保 安全 监督 抽查 提 质量 案件 查处 惩 违法 信用 体系 建 长效 推动 农资 市场 秩序 持续 好转 保障 农业 生产 安全 和 农产品 质量 安全<br>
 
  __label__0 , 一 指导 思想 根据 中央 和 省市 关于 继续 深入 开展 党 的 群众 路线 教育 实践 活动 的 部署 要求 以及 省市 农业 农村 工作 会议 精神 围绕 促进 农民 增收 改善 农民 生活 维护 农民 权益 全市 农经 系统 转变 作风 上下 联动 扎实 为 农民 办 实事 做 好事 确保 党 的 强农 惠农 政策 落到实处 切实 解决 农民 生产 生活 中 的 实际 问题 坚决 纠正 损害 农民 利益 的 不正之风 以 实际 行动 践行 党 的 群众 路线 二 实事 内容 一 全面 落实 各项 强 农惠农 补贴 政策 深入 宣传 2014年 中央 和 省委 一 号 文件 及 中央 和 全省 农村 工作 会议 全国 和 全省 农业 工作 会议 精神 认真 落实 水稻 直补 良种 补贴 农资 综合 补贴 奶牛 和 生猪 良种 补贴 等 强农 惠农 政策 推动 政策 的 贯彻 落实 二 继续 开展 一 事 一 议 财政 奖补 项目 结合 村庄 规划 和 人居 环境 治理 农村 生活 环境 和 村容村貌 整治 等 实际 改善 农村 生产 生活 条件 提高 农民 生活 质量<br>
 
  Each data consists of label and content. <br>

  The labels start with a special string __label__ following with the serial number of the label name which are saved in a file called 'label_dict.json'.<br>

  The contents are splited already by tokenizer.<br>

  The train data and test data locate in /data/*<br>

## Model

  The model used in this project is fastText , you can run train.py directly to train the model which will be saved as model/fasttext.bin.
  The training result is as below<br>

 办公;, precison:0.9845, recall:0.9859789684526791, F1:0.9852389291968977<br>
 财经;, precison:0.9005, recall:0.9009504752376188, F1:0.9007251812953239<br>
 军事;, precison:0.9475, recall:0.9921465968586387, F1:0.969309462915601<br>
 其他;, precison:0.6795, recall:0.9295485636114911, F1:0.7850953206239167<br>
 政务;, precison:0.9475, recall:0.8326010544815465, F1:0.8863423760523854<br>
 科技;, precison:0.9975, recall:0.8467741935483871, F1:0.915977961432507<br>
 
## Predict

  Run predict.py to predict input text and the example is as following.<br>
 
  Please input sentence: 新华08网上海6月28日电(记者有之炘)日前，中国与巴西也达成了货币互换协议意向，两国将于未来数周之内正式签署1900亿人民币的货币互换协议，协议有效期将达十年｡中巴双边贸易往来日益密切，自2009年起，中国超过美国跃升为巴西最大的贸易伙伴｡数据显示，2011年巴西向中国出口了443亿美元的商品，同比增长43.9%｡与此同时，中国成为巴西的第二大进口来源国｡澳大利亚和新西兰是发达国家中最早与中国签订人民币互换协议的央行，阿联酋和土耳其央行也在今年第一季度与中国央行签订了货币互换协议｡截至今年三月份，中国已经和19个国家建立了货币互换关系，涉及金额达16000亿元人民币｡在美元和欧元都不景气的情况下，现在正是推行人民币国际化的最佳时机｡据悉，继日元和人民币直接兑换开启后，澳元、韩元等货币也有望加入这一行列｡澳新银行大中华区经济研究总监刘利刚认为，这将增加人民币作为贸易货币的国际重要性，并逐步提升人民币作为融资货币的可能性，推进人民币成为国际储备货币｡<br>
  
  result: /财经;<br>













  


  
 



