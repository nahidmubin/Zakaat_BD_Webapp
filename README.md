# Introduction

Zakaat BD is a Website that calculates Zakaat for people living in Bangladesh where one don't have to know the Gold and Silver price. It automatically retrieves Gold and Silver prices from BAJUS's website and calculate the nisaab(Threshold Price) and the price of your Gold and Silver. This website isn't applicable for people outside of Bangladesh. This Website was made as a hobby project. Use this website for rough estimation of Zakaat. Please consult with a scholar or an expert for the final estimation.

You can use the website live here: [Zakaat BD](https://zakaatbd.onrender.com)

![ZakaatBD Website Front Page](/front_page_image.jpg)

# Technology Used
This website has been developed with htmx and bootstrap has been used at the frontend and django at the backend.

# Notes
- Gold and Silver Prices are extracted from Bangladesh Jewellers Association's website.
- Selling price for Gold and Silver is taken as 20% less than the Buying price as this is rule in Bangladesh.
- 24K Gold and Silver price are extrapolated from 22K Gold and Silver price respectively.
- 1 Vori is taken as to be 11.664 gram.
- Threshold of Zakaat for Gold is taken as 20 Mithqaal i.e. 85 grams of Pure Gold.
- Threshold of Zakaat for Silver is taken as 200 Dirham i.e. 595 grams of Pure Silver.
- Zakaat amount is 2.5% of the Zakaatable asset.

- Threshold values in gram that has been used in this website, is according to Shaykh Salih Al-Munajjid's IslamQA website. According to Mufti Yusuf Sultan these values are 87.48 gram and 612.36 gram for Gold and Silver respectively. Check the refernces for details.

# References
1. [BAJUS's Gold and Silver Price](https://www.bajus.org/gold-price)
2. [How to Calculate Zakah on Gold -islamqa](https://islamqa.info/en/answers/214221/)
3. [Minimum amount (nisab) required to pay zakat in dollars -islamqa](https://islamqa.info/bn/answers/64/)
4. [Evidence That the Rate of Zakah is 2.5% -islamqa](https://islamqa.info/bn/answers/145600/)
5. [ইসলামী অর্থনীতিতে যাকাতের ভূমিকা ও যাকাতের খুঁটিনাটি](https://yousufsultan.com/zakat-in-details/)
6. [যাকাত কীভাবে হিসাব করতে হয়? ইউসুফ সুলতান](https://www.youtube.com/watch?v=bW4oyoUd7TM)
7. [যাকাত কাকে দেয়া যায়? ইউসুফ সুলতান](https://www.youtube.com/watch?v=b3qcSUeUx2U)
8. [যাকাত হিসাব করার টেমপ্লেট - গুগল / এক্সেল শিট](https://www.youtube.com/watch?v=_YgN_LAfKrA)
9. [Mufti Yousuf Sultan's Zakaat Template link - Google Sheet](https://goo.gl/3c5c6D)
10. [Mufti Yousuf Sultan's Zakaat Template link - Excel](https://goo.gl/e9NbkT)