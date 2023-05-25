

from konlpy.tag import Kkma
from konlpy.utils import pprint
from gensim.models.word2vec import Word2Vec

# import warnings
# warnings.filterwarnings("ignore")


# data = [["KB±İÀ¶ÁöÁÖ°¡ KBÁõ±Ç, KBÄ³ÇÇÅ», KBºÎµ¿»ê½ÅÅ¹ µî 3°³ °è¿­»ç ´ëÇ¥¸¦ »õ·Î ¼±Á¤Çß´Ù. °¡Àå Å« °ü½ÉÀÌ ½ò·È´ø KBÁõ±Ç ´ëÇ¥ÀÌ»ç ÈÄº¸¿¡´Â ¹ÚÁ¤¸² KBÁõ±Ç ºÎ»çÀå °â KB±¹¹ÎÀºÇà ºÎÇàÀåÀ» ¼±Á¤Çß´Ù. ¹Ú ÈÄº¸°¡ ÁÖÁÖÃÑÈ¸ µîÀ» °ÅÃÄ ÃÖÁ¾ ¼±ÀÓµÇ¸é ±İÀ¶ÅõÀÚ¾÷°è ÃÖÃÊ ¿©¼º ÃÖ°í°æ¿µÀÚ(CEO)°¡ µîÀåÇÑ´Ù. KB±İÀ¶Àº 19ÀÏ °è¿­»ç ´ëÇ¥ÀÌ»çÈÄº¸ ÃßÃµÀ§¿øÈ¸(ÀÌÇÏ ´ëÃßÀ§)¸¦ ¿­°í KBÁõ±Ç¡¤KBÄ³ÇÇÅ»¡¤KBºÎµ¿»ê½ÅÅ¹ µî 7°³ °è¿­»ç ´ëÇ¥ ÈÄº¸¸¦ ¼±Á¤Çß´Ù°í ¹àÇû´Ù. KBÁõ±Ç ½ÅÀÓ ´ëÇ¥ÀÌ»ç ÈÄº¸¿¡´Â ¹ÚÁ¤¸² KBÁõ±Ç ºÎ»çÀå °â KB±¹¹ÎÀºÇà ºÎÇàÀå°ú ±è¼ºÇö KBÁõ±Ç ºÎ»çÀåÀ» ÃßÃµÇß´Ù. KBÁõ±ÇÀº ±âÁ¸ÀÇ º¹¼ö ´ëÇ¥Ã¼Á¦¸¦ À¯ÁöÇÑ´Ù. KBÄ³ÇÇÅ»¿¡´Â È²¼ö³² KBÄ³ÇÇÅ» Àü¹«, KBºÎµ¿»ê½ÅÅ¹¿¡´Â ±èÃ»°â KB±¹¹ÎÀºÇà ¿µµîÆ÷ Áö¿ª¿µ¾÷±×·ì´ëÇ¥°¡ °¢°¢ ´ëÇ¥ÀÌ»ç ÈÄº¸·Î ¼±Á¤µÆ´Ù. ¾çÁ¾Èñ KB¼ÕÇØº¸Çè ´ëÇ¥, Á¶Àç¹Î¡¤ÀÌÇö½Â KBÀÚ»ê¿î¿ë ´ëÇ¥, ±èÇØ°æ KB½Å¿ëÁ¤º¸ ´ëÇ¥´Â Àç¼±Á¤µÆ´Ù. KBµ¥ÀÌÅ¸½Ã½ºÅÛÀº ÀÌ¸¥ ½ÃÀÏ ³»¿¡ ÀûÇÕÇÑ ÀÎ»ç¸¦ Ã£¾Æ ÃßÈÄ ÃßÃµÇÒ °èÈ¹ÀÌ´Ù. ¹ÚÁ¤¸² ºÎ»çÀåÀÌ KBÁõ±Ç ´ëÇ¥¿¡ ÃëÀÓÇÏ¸é Áõ±Ç»ç ÃÖÃÊ·Î ¿©¼º CEO°¡ Åº»ıÇÑ´Ù. ¹Ú ÈÄº¸´Â KB±İÀ¶ÁöÁÖ¿¡¼­ WM(ÀÚ»ê°ü¸®)°ú ¸®½ºÅ©, ¿©½Å µî ¿äÁ÷À» µÎ·ç °ÅÃÆ´Ù. ±×·ì WM ºÎ¹® ½Ã³ÊÁö¿µ¾÷À» ÀÌ²ø¸ç ¸®´õ½ÊÀ» ¹ßÈÖÇÏ°í ÀÖ´Ù´Â Á¡À» ³ô°Ô Æò°¡ ¹Ş´Â´Ù. ±è¼ºÇö ºÎ»çÀåÀº ´ëÇ¥ÀûÀÎ ÅõÀÚÀºÇà(IB) Àü¹®°¡´Ù. ÅõÀÚÀÚ»ê ´Ùº¯È­¸¦ ÅëÇØ ½ÃÀå ÁöÀ§¸¦ ¹Ù²Ü ¼ö ÀÖ´Â ¸®´õ½ÊÀ» °®Ãè´Ù´Â Æò°¡¸¦ ¹Ş´Â´Ù. ½ÅÀÓ ´ëÇ¥´Â 20¡­21ÀÏ °è¿­»ç ´ëÇ¥ÀÌ»çÈÄº¸ ÃßÃµÀ§¿øÈ¸ÀÇ ÃÖÁ¾ ½É»ç¿Í ÃßÃµÀ» °ÅÃÄ ÁÖÁÖÃÑÈ¸¿¡¼­ È®Á¤ÇÒ °èÈ¹ÀÌ´Ù. ½ÅÀÓ ´ëÇ¥ ÀÓ±â´Â 2³â, Àç¼±Á¤ ´ëÇ¥ ÀÓ±â´Â 1³âÀÌ´Ù."],
# ["¼­¿ï ¿©ÀÇµµ¿¡¼­ ¡®Ä«Ä«¿À Ä«Ç®¡¯¿¡ ¹İ´ëÇÏ´Â Àü±¹ ÅÃ½Ã¾÷°è °ü°èÀÚµéÀÌ 20ÀÏ ´ë±Ô¸ğ ÁıÈ¸¸¦ ¹úÀÎ´Ù. ÅÃ½Ã±â»ç ÃÖ ¸ğ ¾¾ÀÇ ºĞ½Å µîÀ» °è±â·Î ¾÷°è°¡ ¡®ÃÑ·ÂÅõÀï¡¯À» ¿¹°íÇÑ °¡¿îµ¥ ÁıÈ¸?½ÃÀ§ ½Ã°£ÀÌ Ãâ?Åğ±Ù ½Ã°£°ú °ãÃÄ ÀÌ ½Ã°¢ ¿©ÀÇµµ ÁÖº¯¿¡ ±Ø½ÉÇÑ ±³ÅëÃ¼ÁõÀÌ ¿¹»óµÈ´Ù. 19ÀÏ °æÂû°ú ÅÃ½Ã¾÷°è µî¿¡ µû¸£¸é 20ÀÏ ¿ÀÈÄ 2½Ã Àü±¹ÅÃ½Ã³ëµ¿Á¶ÇÕ¿¬¸Í, Àü±¹¹ÎÁÖÅÃ½Ã³ëµ¿Á¶ÇÕ¿¬¸Í, Àü±¹°³ÀÎÅÃ½Ã¿î¼Û»ç¾÷Á¶ÇÕ¿¬ÇÕÈ¸ µî 4°³ ´ÜÃ¼°¡ ¼­¿ï ¿©ÀÇµµ ±¹È¸ ¾Õ ÀÇ»ç´ç´ë·Î¿¡¼­ 3Â÷ ÁıÈ¸¸¦ ¿¬´Ù. °­½ÅÇ¥ Àü±¹ÅÃ½Ã³ëµ¿Á¶ÇÕ¿¬¸Í À§¿øÀåÀº ÁıÈ¸¸¦ ÇÏ·ç ¾ÕµÎ°í ¿­¸° ±âÀÚÈ¸°ß¿¡¼­ ¡°Á×µçÁö »ìµçÁö ÃÑ·Â ÅõÀïÀ» ÇÒ °Í¡±ÀÌ¶ó°í ¸»Çß´Ù. ¡®±¹È¸¸¦ Æ÷À§ÇÏ°Ú´Ù´ø ±âÁ¸ °èÈ¹Àº ±×´ë·Î ÁøÇàµÇ´À³Ä¡¯´Â Áú¹®¿¡ °­ À§¿øÀåÀº ¡°±×·¸´Ù¡±¸é¼­µµ ¡°¸¸¾à (°æÂûÀÌ) ¸·À¸¸é ÇÒ ¼ö ¾ø°ÚÁö¸¸, ÇÏ´Â µ¥±îÁö ÃÖ¼±À» ´ÙÇØ ÀûÆó 1È£ÀÎ ±¹È¸¸¦ ¹İµå½Ã ½ÉÆÇÇÒ °Í¡±ÀÌ¶ó°í °­Á¶Çß´Ù. °­ À§¿øÀåÀº ¡°³»ÀÏÀº Á¦ÁÖµµ¸¦ Æ÷ÇÔÇÑ Àü±¹ÀÇ ÅÃ½Ã°¡ ¿îÇàÀ» ÁßÁöÇÑ´Ù¡±¸ç ¡°¾ÕÀ¸·Î 4Â÷, 5Â÷ ÁıÈ¸ ÀÏÁ¤ÀÌ ÀâÈ÷¸é ±× ³¯¸¶´Ù ÅÃ½Ã ¿îÇàÀÌ Á¤ÁöµÉ °Í¡±ÀÌ¶ó°í ¸»Çß´Ù. ÀÌ¾î ¡°ÀÚ²Ù ½Ã¹Î¿¡°Ô ºÒÆíÀ» µå·ÁÁË¼ÛÇÏÁö¸¸ »ıÁ¸±ÇÀ» ÁöÅ°±â À§ÇØ ¿©ÀÇµµ ±¹È¸ ¾Õ¿¡ ¸ğÀÏ ¼ö¹Û¿¡ ¾ø´Â Àı¹ÚÇÑ »óÈ²À» Çì¾Æ·Á ÁÖ½Ã±æ ¹Ù¶õ´Ù¡±°í µ¡ºÙ¿´´Ù."],
#        ["'³»º¸Çè Ã£¾ÆÁÜ' È¨ÆäÀÌÁö°¡ Á¢¼ÓÀÚ ÆøÁÖ·Î ÀÎÇØ Á¢¼Ó ´ë±â½Ã°£ÀÌ ±æ¾îÁö°í ÀÖ´Ù. 19ÀÏ ¿ÀÈÄ 9½Ã20ºĞ ÇöÀç '³»º¸Çè Ã£¾ÆÁÜ' È¨ÆäÀÌÁö¿¡´Â Á¢¼ÓÀÚ ¼ö°¡ ¸ô¸®¸ç ¼­ºñ½º ÀÌ¿ëÀÌ ºÒ°¡´ÉÇÑ »óÅÂ´Ù. ÇöÀç »çÀÌÆ® Á¢¼ÓÀÚ ¼ö´Â 4641¿©¸í¿¡ ´ŞÇÑ´Ù. ±İ°¨¿ø¿¡ µû¸£¸é 11¿ù ¸» ±âÁØ ¼ÒºñÀÚ°¡ Ã£¾Æ°¡Áö ¾ÊÀº ¼ûÀº º¸Çè±İÀº ¾à 9Á¶8130¾ï¿øÀÎ °ÍÀ¸·Î ³ªÅ¸³µ´Ù.Áö³­ÇØ 12¿ùºÎÅÍ Áö³­´Ş±îÁö ¼ûÀºº¸Çè±İ Ã£¾ÆÁÖ±â ¾È³» È°µ¿À» ÅëÇØ ¾à 3Á¶125¾ï¿ø(240¸¸5000°Ç)ÀÌ ÁÖÀÎÀ» Ã£¾Ò´Ù. ¾÷±Çº°·Î´Â »ı¸íº¸ÇèÈ¸»ç°¡ ¾à 2Á¶7907¾ï¿ø(222¸¸°Ç), ¼ÕÇØº¸ÇèÈ¸»ç°¡ 2218¾ï¿ø(18¸¸ 5000°Ç)À» Ã£¾ÆÁá´Ù. ±İ°¨¿øÀº 20ÀÏºÎÅÍ ±âÁ¸ '³»º¸Çè Ã£¾ÆÁÜ' ¼­ºñ½º¸¦ °³¼±ÇØ Ã£Àº ¼ûÀºº¸Çè±İÀ» °¢ º¸ÇèÈ¸»ç ¿Â¶óÀÎ Ã»±¸½Ã½ºÅÛ¿¡ ¹Ù·Î Á¢¼ÓÇÒ ¼öÀÖµµ·Ï ¸µÅ©¸¦ Á¦°øÇÑ´Ù°í ¹àÇû´Ù. ±âÁ¸ ¼ûÀº º¸Çè±İ Ã»±¸ ½Ã¿¡´Â ¼ÒºñÀÚ°¡ °³º°ÀûÀ¸·Î ÇØ´ç º¸ÇèÈ¸»ç È¨ÆäÀÌÁö, Äİ¼¾ÅÍ, °è¾à À¯Áö¡¤°ü¸® ´ã´ç ¼³°è»ç µîÀ» Ã£¾Æ º°µµ·Î ÁøÇàÇØ¾ß ÇÏ´Â ºÒÆíÀÌ ÀÖ¾ú´Ù. ¾ÕÀ¸·Î´Â '³»º¸Çè Ã£¾ÆÁÜ' È¨ÆäÀÌÁö¿¡ Á¢¼ÓÇØ ÀÌ¸§, ÈŞ´ëÆù ¹øÈ£, ÁÖ¹Îµî·Ï¹øÈ£¸¦ ÀÔ·Â ÈÄ ÈŞ´ëÆù ÀÎÁõÀ» °ÅÄ¡¸é »ı¸íº¸Çè 25°³»ç, ¼ÕÇØº¸Çè 16°³»ç µî ¸ğµÎ 41°³ º¸ÇèÈ¸»ç¸¦ ´ë»óÀ¸·Î ¼ûÀº º¸Çè±İÀ» Á¶È¸ÇÒ ¼ö ÀÖ´Ù. ¼ûÀº º¸Çè±İÀÌ ÀÖ´Â °æ¿ì ÇØ´ç º¸Çè»ç¿¡ º¸Çè±İ Áö±ŞÃ»±¸¸¦ ÇÏ¸é ¿µ¾÷ÀÏ 3ÀÏ ÀÌ³» ±İ¾×À» Áö±ŞÇÑ´Ù. ´Ü ÀÌ¹Ì º¸Çè±İÀ» Ã»±¸ÇØ ½É»ç ÁßÀÌ°Å³ª Áö±ŞÁ¤Áö µîÀ¸·Î Ã»±¸ÇÒ ¼ö ¾ø´Â º¸Çè±İÀº Á¶È¸µÇÁö ¾Ê´Â´Ù."],
#        ["KBÁõ±ÇÀº ±è¼ºÇö KBÁõ±Ç IBÃÑ°ı ºÎ»çÀå°ú ¹ÚÁ¤¸² KBÁõ±Ç WM ºÎ¹® ºÎ»çÀåÀ» ½ÅÀÓ ´ëÇ¥·Î °¢°¢ ¼±ÀÓÇß´Ù°í 19ÀÏ ¹àÇû´Ù. À±°æÀº, Àüº´Á¶ ´ëÇ¥ÀÌ»ç°¡ ÀÚ¸®¿¡¼­ ¹°·¯³µÁö¸¸ °¢ÀÚ ´ëÇ¥ÀÌ»ç Ã¼Á¦´Â À¯ÁöµÈ´Ù. ÀÌ´Â WM°ú IBÀÇ ºÎ¹®À» °¢°¢ ÁıÁßÇÏ±â À§ÇÔÀ¸·Î Ç®ÀÌµÈ´Ù. Æ¯È÷ ¹Ú ½ÅÀÓ ´ëÇ¥´Â Áõ±Ç¾÷°è Ã¹ ¿©¼º ÃÖ°í°æ¿µÀÚ(CEO)ÀÌ´Ù. ¹Ú ½ÅÀÓ ´ëÇ¥´Â ¼­¿ï´ë °æ¿µÇĞ°ú¡¤°æ¿µ´ëÇĞ¿ø Ãâ½ÅÀ¸·Î 1986³â Ã¼ÀÌ½º¸ÇÇØÆ° ¼­¿ïÁöÁ¡, Á¶ÈïÀºÇà, »ï¼ºÈ­Àç µîÀ» °ÅÃÄ 2004³â Ã³À½À¸·Î KB±¹¹ÎÀºÇà¿¡ µé¾î¿Ô´Ù. ´ç½Ã ½ÃÀå¿î¿µ¸®½ºÅ© ºÎÀåÀ» ½ÃÀÛÀ¸·Î 2012³â¿£ WMº»ºÎÀå, 2014³â ¸®½ºÅ©°ü¸®±×·ì ºÎÇàÀå, 2015³â KB±İÀ¶ÁöÁÖ ¸®½ºÅ©°ü¸®Ã¥ÀÓÀÚ ºÎ»çÀå °â ¸®½ºÅ©°ü¸®±×·ì ºÎÇàÀåÀ» ¸Ã¾Ò°í 2016³â¿£ ¿©½Å±×·ì ºÎÇàÀåÀ» ¸Ã¾Ò´Ù. ÀÛ³âºÎÅÏ KB±İÀ¶ WMÃÑ°ı ºÎ»çÀå °â ÀºÇà WM±×·ì ºÎÇàÀå °â KBÁõ±Ç WMºÎ¹® ºÎ»çÀåÀ» ¸Ã°í ÀÖ´Ù. KB±İÀ¶ÁöÁÖ´Â ¹Ú ½ÅÀÓ ´ëÇ¥¿¡ ´ëÇØ WM, ¸®½ºÅ©, ¿©½Å µî Æø³ĞÀº ¾÷¹« °æÇèÀ» ¹ÙÅÁÀ¸·Î ¼öÀÍ È®´ë¿¡ ´ëÇÑ ½ÇÇà¿ª·®À» º¸À¯ÇÏ°í ÀÖ´Ù°í ¹àÇû´Ù. ±×·ì WM ºÎ¹®ÀÇ ½Ã³ÊÁö¿µ¾÷À» ÁøµÎÁöÈÖÇÏ¸ç ¸®´õ½ÊÀ» ¹ßÈÖÇß´Ù´Â Æò°¡´Ù. Çö IBÃÑ°ı ºÎ»çÀåÀÎ ±è¼ºÇö ½ÅÀÓ ´ëÇ¥´Â IBºÎ¹®À» ÃÑ°ıÇÑ´Ù. ±è ½ÅÀÓ ´ëÇ¥ÀÌ»ç´Â ¿¬¼¼´ë °æÁ¦ÇĞ°ú¸¦ Á¹¾÷ÇÏ°í 1988³â ´ë½ÅÁõ±Ç¿¡ ÀÔ»çÇÑ ÀÌÈÄ ÇÑ´©¸®ÅõÀÚÁõ±ÇÀ» °ÅÃÄ 2008³â KBÅõÀÚÁõ±Ç ±â¾÷±İÀ¶º»ºÎÀåÀ¸·Î ÀÓ¸íµÆ´Ù. ÀÌÈÄ 2015³âºÎÅÍ KBÅõÀÚÁõ±Ç IBºÎ¹®¿¡¼­ ÀÏÇÑ Àü¹®°¡´Ù. KB±İÀ¶ÁöÁÖ´Â ±è ½ÅÀÓ ´ëÇ¥¿¡ ´ëÇØ IB Àü¹®°¡·Î ÅõÀÚÀÚ»ê ´Ùº¯È­ µîÀ» ÅëÇØ ½ÃÀå ÁöÀ§¸¦ °³¼±½ÃÅ³ ¼ö ÀÖ´Â °ËÁõµÈ ¸®´õ½ÊÀ» º¸À¯Çß´Ù°í Æò°¡Çß´Ù."], 
#         ["""¼­¹Î±İÀ¶ÁøÈï¿øÀº Áö³­ 18ÀÏ ¼­¿ï Ã»°èÃµ·Î º»¿ø¿¡¼­ Á¦2Â÷ ¼­¹Î±İÀ¶ Àü¹®°¡ °£´ãÈ¸¸¦ °³ÃÖÇß´Ù¼Ò 19ÀÏ ¹àÇû´Ù.

# ÀÌ¹ø °£´ãÈ¸´Â ¼­¹Î±İÀ¶, º¹Áö, ÀÚÈ°»ç¾÷ µî °¢ ºĞ¾ß Àü¹®°¡µéÀÌ Âü¼®ÇÑ °¡¿îµ¥, Á¤Ã¥¼­¹Î±İÀ¶ Áö¿øÀÇ ¹æÇâ¼º¿¡ ´ëÇØ¼­ ÀÇ°ßÀ» Ã»ÃëÇÏ±â À§ÇØ ¸¶·ÃµÆ´Ù. ÀÌ³¯ ÀÌ ¿øÀåÀº "¼Òµæ¾ç±ØÈ­¿Í °í¿ëºÎÁø ½ÉÈ­ µîÀ¸·Î ¼­¹Î¡¤Ãë¾à°èÃş, ÀÚ¿µ¾÷ÀÚµéÀÇ °æÁ¦Àû ¾î·Á¿òÀÌ Ä¿Áö´Â °¡¿îµ¥ »çÈ¸¾ÈÀü¸ÁÀ¸·Î¼­ ¼­¹Î±İÀ¶ÀÇ ¿ªÇÒÀÌ Áß¿äÇÑ ½ÃÁ¡"ÀÌ¶ó¸ç, "ÇöÀç 8µî±Ş ÀÌÇÏÀÚ°¡ 263¸¸¸íÀÌ°í ÀÌµéÁß 74%°¡ ¿¬Ã¼ÁßÀÎ »óÈ²¿¡¼­ Á¤»óÀûÀÎ ±İÀ¶ ÀÌ¿ëÀÌ ¾î·Á¿î Ãë¾à°èÃş¿¡°Ô ²À ÇÊ¿äÇÑ ¼­¹Î±İÀ¶ Áö¿øÀ» À§ÇØ ³ë·ÂÇØ¾ß ÇÑ´Ù"°í °­Á¶Çß´Ù.

# ÀÌ¾î¼­ ÀÌ ¿øÀåÀº "ÇöÀå Àü¹®°¡ÀÇ ÀÇ°ßÀ» ¹İ¿µÇÏ¿© Ãë¾à°èÃşÀ» À§ÇÑ ±İÀ¶°ú ÇÔ²² ±İÀ¶±³À°, ÄÁ¼³ÆÃ, Á¾ÇÕ»ó´ã µî ÀÚÈ°±â¹İÀ» ±¸ÃàÇÏµµ·Ï Èû¾²°Ú´Ù"°í ¹àÇû´Ù. ÀÌ³¯ Âü¼®ÀÚµéÀº 'Á¤Ã¥¼­¹Î±İÀ¶Áö¿ø¿¡ ´ëÇÑ ¹æÇâ¼º'¿¡ ´ëÇÏ¿© ´Ù¾çÇÑ ÀÇ°ßÀ» Á¦½ÃÇß´Ù.

# ÁøÈï¿øÀº ÀÌ³¯ °£´ãÈ¸ÀÇ ´Ù¾çÇÑ Á¦¾ğµéÀ» ¹ÙÅÁÀ¸·Î ¼ö¿äÀÚ°¡ Ã¼°¨ÇÒ ¼ö ÀÖ´Â ½ÇÁúÀûÀÎ ¹æ¾È ¸¶·ÃÀ» À§ÇØ ´õ¿í ³ë·ÂÇÏ°í, Áö¼ÓÀûÀ¸·Î ¼­¹Î±İÀ¶ ÇöÀåÀÇ Æø³ĞÀº ÀÇ°ßÀ» Ã»ÃëÇÒ °èÈ¹ÀÌ´Ù.
# """],
#        ["""JB±İÀ¶ÁöÁÖ´Â Â÷±â È¸Àå ÈÄº¸ÀÚ·Î ±è±âÈ« JBÀÚ»ê¿î¿ë ´ëÇ¥(»çÁø)¸¦ ¼±Á¤Çß´Ù.

# 19ÀÏ JB±İÀ¶ÁöÁÖ ÀÓ¿øÈÄº¸ÃßÃµÀ§¿øÈ¸´Â ÃÖÁ¾ ÈÄº¸±º¿¡ ´ëÇØ PT¹ßÇ¥¿Í ½ÉÃş¸éÁ¢À» ÁøÇàÇÑ ÈÄ, ±è ´ëÇ¥¸¦ ÃÖÁ¾ ÈÄº¸ÀÚ·Î ¼±Á¤Çß´Ù.

# ÀÌ³¯ PT¹ßÇ¥¿Í ½ÉÃş¸éÁ¢¿¡¼± ÈÄº¸ÀÚÀÇ JB±İÀ¶±×·ìÀÇ ¼ºÀå ºñÀü°ú Àü¹®¼º, ¸®´õ½Ê, ±â¾÷ÀÇ »çÈ¸Àû Ã¥ÀÓ µî ÈÄº¸ÀÚÀÇ ¿ª·®¿¡ ´ëÇØ Æò°¡ÇßÀ¸¸ç, ±è ´ëÇ¥´Â ÀºÇàÀ» ºñ·Ô º¸Çè»ç, ÀÚ»ê¿î¿ë»ç µî ±İÀ¶±Ç ÀÓ¿ø °æÇèÀ» ¹ÙÅÁÀ¸·Î ±İÀ¶ Àü¹İ¿¡ ´ëÇÑ Àü¹®ÀûÀÎ Áö½Ä°ú ³ĞÀº ½Ä°ßÀ» °®Ãß°í ÀÖ´Ù´Â Á¡ÀÌ ³ôÀÌ Æò°¡µÆ´Ù.

# JB±İÀ¶ÁöÁÖ ÀÓÃßÀ§ °ü°èÀÚ´Â "±è ÈÄº¸ÀÚ°¡ 20³â ÀÌ»ó ±İÀ¶»ê¾÷¿¡ Á¾»çÇÑ °æÇèÀ» ¹ÙÅÁÀ¸·Î ±İÀ¶¿¡ ´ëÇÑ Àü¹®ÀûÀÎ ½Ä°ß »Ó ¸¸ ¾Æ´Ï¶ó ¸®´õ½Ê°ú ¼ÒÅë´É·Âµµ Å¹¿ùÇÏ´Ù"¸ç "±Şº¯ÇÏ´Â ±İÀ¶È¯°æ¿¡ ´ëÀÀÇÏ°í °è¿­»ç °£ ½Ã³ÊÁö Ã¢ÃâÀ» ÅëÇØ ±â¾÷°¡Ä¡¸¦ ±Ø´ëÈ­ÇÏ´Â µî JB±İÀ¶±×·ìÀ» ÃÖ°íÀÇ ¼Ò¸ÅÀü¹® ±İÀ¶±×·ìÀ¸·Î ¹ßÀü½ÃÅ³ ÀûÀÓÀÚ"¶ó°í ¹àÇû´Ù. ÀÌ¿¡ µû¶ó ±è ³»Á¤ÀÚ´Â ³»³â 3¿ù Á¤±âÁÖÁÖÃÑÈ¸¿Í ÀÌ»çÈ¸¸¦ °ÅÃÄ ´ëÇ¥ÀÌ»ç È¸ÀåÀ¸·Î ¼±ÀÓ µÉ ¿¹Á¤ÀÌ´Ù.
# """], 
#         ["""1800¸¸ ±Ù·ÎÀÚÀÇ 2018³â ±Í¼Ó ±Ù·Î¼Òµæ¿¡ ´ëÇÑ ¿¬¸»Á¤»ê ½Å°í±â°£ÀÌ ÇÑ ´Ş¿© ¾ÕÀ¸·Î ´Ù°¡¿Ô´Ù.

# ¿ÃÇØ ¿¬¸»Á¤»ê¿¡´Â Áß¼Ò±â¾÷ Ãë¾÷ Ã»³â¿¡ ´ëÇÑ ¼Òµæ¼¼ °¨¸éÀÌ È®´ëµÇ°í µµ¼­¡¤°ø¿¬ºñ ÁöÃâ¾×¿¡ ´ëÇÑ ½Å¿ëÄ«µå »ç¿ë¾×¿¡ ¼Òµæ°øÁ¦°¡ Àû¿ëµÇ´Â µî »õ·Î¿î ±âÁØÀÌ Àû¿ëµÇ±â ¶§¹®¿¡ ¹Ù²ï °øÁ¦ ±âÁØÀ» ²Ä²ÄÈ÷ Ã¬±â´Â °ÍÀÌ Áß¿äÇÏ´Ù.

# ±¹¼¼Ã»Àº ¿ÃÇØ ±Ù·Î¼ÒµæÀÌ ¹ß»ıÇÑ ±Ù·ÎÀÚ´Â ³»³â 2¿ùºĞ ±Ş¿©¸¦ Áö±Ş¹ŞÀ» ¶§±îÁö ¿¬¸»Á¤»êÀ» ½Å°íÇØ¾ß ÇÑ´Ù°í 20ÀÏ ¹àÇû´Ù.

# ¡Ş¿ÃÇØºÎÅÍ ´Ş¶óÁö´Â ÁÖ¿ä °øÁ¦ Ç×¸ñ

# ¿ÃÇØ ¿¬¸»Á¤»êºÎÅÍ´Â Áß¼Ò±â¾÷ Ãë¾÷ Ã»³â¿¡ ´ëÇÑ ¼Òµæ¼¼ °¨¸éÀ» ¹ŞÀ» ¼ö ÀÖ´Â ´ë»ó ¿¬·ÉÀÌ ±âÁ¸ 29¼¼¿¡¼­ 34¼¼·Î È®´ëµÈ´Ù. °¨¸éÀ²µµ 70%¿¡¼­ 90%·Î È®´ëµÇ°í °¨¸é Àû¿ë±â°£µµ 3³â¿¡¼­ 5³âÀ¸·Î È®´ëµÈ´Ù.

# ÃÑ±Ş¿©¾× 7000¸¸¿ø ÀÌÇÏ ±Ù·ÎÀÚ´Â µµ¼­¡¤°ø¿¬ºñ¸¦ ½Å¿ëÄ«µå·Î °áÁ¦ÇÑ °æ¿ì ÇØ´ç ºñ¿ëÀ» ÃÖ´ë 100¸¸¿ø±îÁö Ãß°¡ ¼Òµæ°øÁ¦ ¹ŞÀ» ¼ö ÀÖ´Ù. ¿Ã 7¿ù1ÀÏ ÀÌÈÄ µµ¼­°ø¿¬ºñ·Î ÁöÃâÇÑ ±İ¾×ÀÇ ¼Òµæ°øÁ¦À² 30%°¡ Àû¿ëµÇ±â ¶§¹®ÀÌ´Ù.

# °Ç°­º¸Çè »êÁ¤Æ¯·Ê ´ë»óÀÚ·Î µî·ÏµÈ ºÎ¾ç°¡Á·À» À§ÇØ ÁöÃâÇÑ ÀÇ·áºñ´Â ±âÁ¸ 700¸¸¿ø ÇÑµµ°¡ ÆóÁöµÇ°í ¿ÃÇØºÎÅÍ Àü¾×°øÁ¦¸¦ ¹ŞÀ» ¼ö ÀÖ°Ô µÆ´Ù.

# ÃÑ±Ş¿©¾×ÀÌ 5500¸¸¿øÀÌ°Å³ª Á¾ÇÕ¼Òµæ±İ¾×ÀÌ 4000¸¸¿ø ÃÊ°ú ±Ù·ÎÀÚÀÇ °æ¿ì ¿ù¼¼¾× ¼¼¾×°øÁ¦À²ÀÌ 10%¿¡¼­ 12%·Î ÀÎ»óµÈ´Ù. ¿ù¼¼¾× ¼¼¾×°øÁ¦ ÇÑµµ´Â 750¸¸¿øÀÌ¸ç ÀÓ´ëÂ÷ °è¾à¼­»ó ÁÖ¼ÒÁö¿Í °è¾à±â°£ µî ³»¿ªÀ» Á¤È®È÷ ±âÀçÇØ¾ß °øÁ¦¸¦ ¹ŞÀ» ¼ö ÀÖ´Ù.

# ÀÓÂ÷º¸Áõ±İ 3¾ï¿ø ÀÌÇÏÀÇ ÁÖÅÃ ÀÓÂ÷º¸Áõ±İ ¹İÈ¯ º¸Áõ º¸Çè·áµµ ¿ÃÇØ ¿¬¸»Á¤»êºÎÅÍ º¸Çè·á ¼¼¾×°øÁ¦¸¦ ¹ŞÀ» ¼ö ÀÖÀ¸¸ç, »ı»êÁ÷ ±Ù·ÎÀÚÀÇ ÃÊ°ú±Ù·Î¼ö´ç ºñ°ú¼¼ Àû¿ë ½Ã ±âÁØÀÌ µÇ´Â ¿ùÁ¤¾× ±Ş¿©¾×Àº 150¸¸¿ø ÀÌÇÏ¿¡¼­ 190¸¸¿ø ÀÌÇÏ·Î »óÇâµÈ´Ù.

# 6¼¼ ÀÌÇÏ ÀÚ³à ¼¼¾×°øÁ¦´Â ¾Æµ¿¼ö´ç Áö±Ş¿¡ µû¶ó ¿ÃÇØºÎÅÍ ÆóÁöµÈ´Ù. ¿Ã ¿¬¸»Á¤»êºÎÅÍ´Â Á¾±³´ÜÃ¼°¡ Á¾±³ÀÎ¿¡°Ô Áö±ŞÇÑ ¼Òµæµµ ½Å°í´ë»ó¿¡ Æ÷ÇÔµÈ´Ù."""]
#        ]
from gensim.models import KeyedVectors
# kkma = Kkma()

# sentences = []
# list_vec = []
# for da in data:
# #     print(da)
#     sentences.append(kkma.sentences(da[0]))
#     for s in sentences:
#         for w in s:
#             list_vec.append(kkma.nouns(w))

# word_list = []
# for l in list_vec:
#     empty_vec = []
#     for w in l:
#         if len(w)>=2:
#             empty_vec.append(w)   
#     word_list.append(empty_vec)        

# import pandas as pd
# f= pd.read_csv(r"C:\Users\mm411\OneDrive\¹ÙÅÁ È­¸é\cralwer\Scrapy\data.tsv","\t")

# with open(r"C:\Users\mm411\OneDrive\¹ÙÅÁ È­¸é\cralwer\Scrapy\data.tsv", 'r') as inp, open('word2vec-format.txt', 'w') as outp:
#     line_count = '...'    # line count of the tsv file (as string)
#     dimensions = '...'    # vector size (as string)
#     outp.write(' '.join([line_count, dimensions]) + '\n')
#     for line in inp:
#         words = line.strip().split()
#         outp.write(' '.join(words) + '\n')
# print(f)
#model = KeyedVectors.load_word2vec_format("Scrapy//ko//ko.bin")
# embedding_model = Word2Vec(word_list, size=100, window = 5, min_count=2, workers=3, iter=1000, sg=1, sample=1e-3)

# from sklearn.cluster import KMeans

# word_vectors = embedding_model.wv.syn0 # ¾îÈÖÀÇ feature vector
# num_clusters = int(word_vectors.shape[0]/50) # ¾îÈÖ Å©±âÀÇ 1/5³ª Æò±Õ 5´Ü¾î
# print(num_clusters)
# num_clusters = int(num_clusters)

# kmeans_clustering = KMeans(n_clusters=num_clusters)
# idx = kmeans_clustering.fit_predict(word_vectors)

# idx = list(idx)
# names = embedding_model.wv.index2word
# word_centroid_map = {names[i]: idx[i] for i in range(len(names))}

# for c in range(num_clusters):
#     # Å¬·¯½ºÅÍ ¹øÈ£¸¦ Ãâ·Â
#     print("\ncluster {}".format(c))
    
#     words = []
#     cluster_values = list(word_centroid_map.values())
#     for i in range(len(cluster_values)):
#         if (cluster_values[i] == c):
#             words.append(list(word_centroid_map.keys())[i])            
#     print(words)


# import chardet    

# with open(r"C:\Users\mm411\OneDrive\¹ÙÅÁ È­¸é\cralwer\Scrapy\NlpModel\nlpmodel.model", 'rb') as rawdata:
#     result = chardet.detect(rawdata.read(10000))

# # check what the character encoding might be
# print(result)

# import pandas as pd

# f=open("word2vec-format.txt","r")
# # print(f)
# from gensim.models import KeyedVectors


# #wv = KeyedVectors.load(r"C:\Users\mm411\OneDrive\¹ÙÅÁ È­¸é\cralwer\Scrapy\kumed-w2v-300.model")
# model = KeyedVectors.load(r"C:\Users\mm411\OneDrive\¹ÙÅÁ È­¸é\cralwer\Scrapy\word2vec-KCC150.model")
# model_result = model.wv.most_similar("ÅÂÇ³")
# print('model_result =', model_result)

# import kss
# # s="È¸»ç µ¿·á ºĞµé°ú ´Ù³à¿Ô´Âµ¥ ºĞÀ§±âµµ ÁÁ°í À½½Äµµ ¸ÀÀÖ¾ú¾î¿ä ´Ù¸¸, °­³² Åä³¢Á¤ÀÌ °­³² ½§½§¹ö°Å °ñ¸ñ±æ·Î Âß ¿Ã¶ó°¡¾ß ÇÏ´Âµ¥ ´Ùµé ½§½§¹ö°ÅÀÇ À¯È¤¿¡ ³Ñ¾î°¥ »· Çß´ä´Ï´Ù °­³²¿ª ¸ÀÁı Åä³¢Á¤ÀÇ ¿ÜºÎ ¸ğ½À."
# # sents=[]
# # for sent in kss.split_sentences(s):
# #     sents.append(sent)

# # print(sents[0])
# # print(sents[1])
# # print(sents[2])
# import re
# pattern = '#([0-9a-zA-Z°¡-ÆR]*)'
# hash_w = re.compile(pattern)

# str="º¯°æ Àü¼Ò¸®µµ ¸øÁö¸£°í ¼Õ ¾È¶³¸®°Ô ³ìÀ½.Áß°£¿¡ ¼¼·Î·Î ¹Ù²å´Âµ¥ÁöÁø³­°Å ¾Æ´¸´Ù¤»¤»#À±±â_½Ã»çÈ¸ https://t.co/7mYslwZIP"
# hash_tag = hash_w.findall(str)
# print("ÇØ½ÃÅÂ±× ÃßÃâ: ", hash_tag)
# for tag in hash_tag:
#     print("tag => ", tag)

# #print(str)


# # str3="2023-02-25 10:00:46+00:00"

# # str3=str3[0:11]+ "{}".format(int(str3.split(" ")[1][0:2])+9)+str3[13:19]
# # print(str3)

# # # str2="2023-02-20T13:38:08.000Z"

# # # str2=str2[:10]+" "+str2[11:19]
# # # print(str2)

# import requests
# from datetime import datetime
# from dateutil.tz import gettz
# from datetime import timedelta
# #from fasttext
# import gensim
# import pymongo
# from flask_cors import CORS
# import random
# import sqlite3
# import MySQLdb
# from mysql.connector import Error 
# from gensim.test.utils import common_texts
# import pandas as pd


# def scheduledTask(number=160,minutes=30):
#     print('ÇĞ½ÀÇÒ µ¥ÀÌÅÍ ÃÖ´ë °³¼ö ÁöÁ¤:',number)
#     dataset = []
#     try:
#         conn=MySQLdb.connect(
#             user="root",
#             passwd="1234",
#             host="localhost",
#             db="crawlerdb"
#            )
#         cursor = conn.cursor()
#         sql = "SELECT snsname,content FROM post"
#         cursor.execute(sql)
#         dataset=list(cursor.fetchall())
#         dataset_naver = []
#         dataset_twitter = []
#         dataset_instargram = []
#         for element in dataset:
#             if element[0] == 'twitter':
#                 dataset_twitter.append(element[1])
#             elif element[0] == 'instagram':
#                 dataset_instargram.append(element[1])
#         dataset = dataset_twitter + dataset_instargram
#         print(dataset)
#         if len(dataset) > number:
#             if len(dataset_instargram) >= int(number/4) and len(dataset_twitter) >= int(number/4) and len(dataset_naver) >= int(number/2):
#                 dataset = random.sample(dataset_instargram,int(number/4)) + random.sample(dataset_twitter,int(number/4)) + random.sample(dataset_naver,int(number/2))
#             elif len(dataset_twitter) >= int(number/7) and len(dataset_naver) >= int(number/3):
#                 dataset = random.sample(dataset_twitter,int(number/7)) + random.sample(dataset_naver,int(number/3))
#             else:
#                 dataset = random.sample(dataset,number)
#         #Ds=pd.DataFrame(dataset,columns=['data'])
#         #Ds.to_csv("save.csv", index = False)
      
#         # trained_dataset = nlp(dataset,model)
#         # trained_number = len(trained_dataset)
#         # print('ÇĞ½ÀµÈ µ¥ÀÌÅÍ °³¼ö',trained_number)

#         # for post in trained_dataset:
#         #      conn.insert_one(post)
#     except Exception as e:
#         print(e)

# scheduledTask()

# import plotly.express as px
# import kss
# from sklearn.cluster import KMeans

# model=  KeyedVectors.load_word2vec_format("word2vec_model_result") # ºÒ·¯¿È

# data_content_all = ['ÄÚ·Î³ª ½Å±Ô È®ÁøÀÚ°¡ ¹ß»ıÇß´Ù.', 'È­Àç°¡ ¹ß»ıÇß´Ù.', 'È«¼ö ÇÇÇØ°¡ ¹ß»ıÇß´Ù.', '»ç°í ³µ´Ù.', '´«ÀÌ ¸¹ÀÌ ³»¸°´Ù.', '»ê¿¡ ºÒÀÌ ³µ´Ù.', 'ºØ±« »ç°í°¡ ¹ß»ıÇÏ´Ù.', 'Æø¹ßÇÏ´Ù.', 'ÅÂÇ³ÀÌ ¹ß»ıÇß´Ù.']
# data_pre = len(data_content_all)

# content_vector = []
# word_vectors = model
# content_vector = word_vectors.get_normed_vectors()



# df=content_vector
# target_label_=[]

# # for i in range(data_pre):
# #  target_label_.append(kmeans.labels_[i])
# print(df)
  
# if len(content_vector) > 200:
#     kmeans = KMeans(n_clusters=10, init='k-means++').fit(content_vector)
# elif len(content_vector)  > 50:
#     kmeans = KMeans(n_clusters=10, init='k-means++').fit(content_vector)
# elif len(content_vector)  > 21:
#     kmeans = KMeans(n_clusters=10, init='k-means++').fit(content_vector)
# fig = px.scatter_3d(
#     df, x='sepal_length', y='sepal_width', z='petal_width',
#     color = kmeans.labels_
# )
# fig.show()



# ## Áö¿ª Ã¼Å© ÇÔ¼ö
# def local_check(str):
#    print(str)





# from konlpy.tag import Kkma
# text="³ª´Â ¹äÀ» ¸Ô´Â´Ù."
# Kkma =  Kkma()

# text=Kkma.nouns(text)
# for i in text:
#     print(i)


# import re
# main_text="#¿À´Ã#³ª´Â ¤»¤»¤»¤»¤»ÀÌ·¶´ÙÁøÂ¥"
# # ''ÅÂ±× ºĞ¸®°úÁ¤
# hashtags=[]
# if '#' in main_text:
#     pattern = '#([0-9a-zA-Z°¡-ÆR]*)'
#     hash_w = re.compile(pattern)
#     hash_tag = hash_w.findall(main_text)
#     for tag in hash_tag:
#            if tag!="":
#                hashtags.append(tag)
#                main_text=main_text.replace('#'+tag,'')


# print(main_text)
# print(hashtags)
# import kss
# # list=['abc','def','ghp']
# str="³ª´Â ¹äÀ» ¸Ô¾ú´Ù ±×·¡¼­ ¿À´Ã"
# list=list+kss.split_sentences(str)
# print(list)

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# import utility.util as util
# import utility.DB_Utility as db
# import numpy as np
# minmaxCountList=db.minmaxCount()[0]
# min=minmaxCountList[0]
# max=minmaxCountList[1]
# CountList=np.array(range(min,max))
# CountList= np.delete(CountList,0)
# print(CountList)
# content="ÄÚ·Î³ª"
# param=('%%%s%%'%content)
# print(param)
# a=db.GetPost(str(14))[0][0]
# print(a)
# post="¾ËÆ®ÄÚÀÎ½ÃÈ²?ºñÆ®ÄÚÀÎ½ÃÈ²¾È³çÇÏ¼¼¿ä?µ¶¼­ÇÏ´ÂÄÚÀÎµ¶ÄÚÀÔ´Ï´ÙÇö?½Ã°¢?¾ËÆ®ÄÚÀÎ?½ÃÈ²¿¡?´ëÇØ?¸»¾¸µå¸®·Á?ÇÕ´Ï´ÙÂü°íÇÏ¼Å¼­?ÅõÀÚÇÏ½Ã±â?¹Ù¶ø´Ï´Ù±İÀÏ?¿ÀÀü?½Ã?°³Àå?Àü¿¡?¸ŞÀÌÀúÄÚÀÎµéÀÌ?¹İµîÇÏ°í?ÀÖ±â?¶§¹®¿¡¾ËÆ®ÄÚÀÎ¿¡?°ü½ÉÀ»?°®°í?ÀÖÀ¸¶ó°í?ÇÏ¿´´ÙÃß°¡¸Å¼ö¸¦?ÇÏ±â¿¡´Â?¾ÆÁ÷?Ãß¼¼?ÀüÈ¯ÀÌ?ÀÏ¾î³ªÁø?¾Ê¾ÒÁö¸¸¼ÕÀıµµ?ÇÒ?ÀÚ¸®°¡?ÀüÇô¾Æ´Ï¶ó°í?ÇÏ¿´´Ù°á·ĞºÎÅÍ?¾ê±âÇÏ¸é?¾ËÆ®ÄÚÀÎµé?´ëºÎºĞÀÌ?¾ÆÁ÷?Ãß¼¼ÀüÈ¯À»?ÇÏ·Á¸é?½Ã°£ÀÌ?ÇÊ¿äÇÏ´Ù°í?»ı°¢ÇÑ´Ù¸Å¸Å?¹æ¹ıÀº?¹Ø¿¡¼­?´Ù½Ã?ÇÑ?¹ø?¾ê±âÇÏ°Ú´ÙÇö?½Ã°¢?¾ËÆ®ÄÚÀÎ?»óÀ§?¸ñ·ÏÀÌ´ÙÇö?½Ã°¢?µî?ÄÚÀÎÀº?¾ÆÀÌÅ¥´Ù¾ÆÀÌÅ¥´Â?¿±ÀüÁÖ¶ó?º¯µ¿¼ºÀÌ?½ÉÇÏÁö¸¸?Â÷Æ®°¡?½ÉÇÏ°Ô?¹«³ÊÁöÁö?¾ÊÀº?ÄÚÀÎ?Áß?ÇÏ³ª´Ù±×·¸´Ù?ÇÏ´õ¶óµµ?ºüÁø?ÆøÀÌ?¿ö³«?Å©±â¿¡?À§¿¡¼­?¸Å¼ö¸¦?µé¾î°£?»ç¶÷Àº?½É°¢ÇÑ?¸¶ÀÌ³Ê½º¸¦?°¡Áö°í?ÀÖÀ¸¸®¶ó?»ı°¢ÇÑ´Ùº»ÀÎµµ?¾ÆÀÌÅ¥¸¦?ºĞÇÒ¸Å¼ö?¹Ş¾Æ¼­?Æò´ÜÀ»?¸ÂÃç?³õ¾Ò¾ú´Ù±İÀÏ?¾ÆÀÌÅ¥°¡?»ó½ÂÇÏ¿©?º»ÀÎÀº?¼ÕÀıÇÏ°í?³ª¿Ô´ÙÃæºĞÈ÷?´õ?¿Ã¶ó°¥?¼ö?ÀÖ´Â?¿©Áö¸¦?°¡Áö°í?ÀÖÁö¸¸Áö±İÀÇ?½ÃÀå»óÈ²À»?Á¾ÇÕÇØº¼?¶§?ÃæºĞÈ÷?´Ù½Ã?ºüÁú?¿©Áö°¡?ÀÖ´Ù°í?»ı°¢ÇÏ¿©´Ù¸¥?ÄÚÀÎÀ¸·Î?ºñÁßÀ»?¿Å°å´Ù?ÁöÇ¥¸¦?º¸¸é?¾ÆÁ÷?°ñµçÅ©·Î½º°¡?¹ß»ıÇÏ±â¿¡?½Ã°£ÀÌ?ÇÊ¿äÇÏ´Ù?»ı°¢ÇÏ¿©?´­¸²?ÀÚ¸®¸¦?ÁØ´Ù¸é?±×?¶§?´Ù½Ã?ÁøÀÔÇØµµ?´ÊÁö?¾Ê°Ú´Ù°í?»ı°¢ÇÏ¿´±â?¶§¹®ÀÌ´ÙÈÄ·«ÃßÃµÁ¾¸ñ°ú?ÀÚ¼¼ÇÑ?¼³¸íÀº?ºí·Î±×¿¡¼­?È®ÀÎÇØÁÖ¼¼¿äÀÎ½ºÅ¸±×·¥?ÇÁ·ÎÇÊ¿¡¼­?ºí·Î±×¸µÅ©¸¦?È®ÀÎÇØÁÖ¼¼¿äµ¶¼­ÇÏ´ÂÄÚÀÎ?µ¶ÄÚ?ºí·Î±×?°æÁ¦ÀûÀÚÀ¯?ºñÆ®ÄÚÀÎ?¾ËÆ®ÄÚÀÎ?ºÎÀÚ?µ¶¼­?ÅõÀÚ?ÄÚÀÎ?°æÁ¦?Áö½Ä?°øÀ¯?¸¹°üºÎ?ºÎÀÚµÇ±â?ÁÖ½Ä?ÅõÀÚ°øºÎ?ºø½æ?¾÷ºñÆ®?ÄÚ·Î³ª?µ¶¼­?Ã¥?Ã¥ÃßÃµ?µ¶¼­ÃßÃµ?¿À´ÃÀÇÅõÀÚ"

# idList=db.findContent(post)
# for index,id in enumerate(idList):
#     postList=db.GetPost(str(id[0]))
#     service=postList[0][0]
#     keyword=postList[0][1]
#     username=postList[0][2]
#     content=postList[0][4]
#     sns=postList[0][5]
#     link=postList[0][6]
#     date=postList[0][7]

print("¾È³ç")