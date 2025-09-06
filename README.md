# onionmail-account-spammer
Spamms onionmail.org accounts to use for whatever, i might be making a script than can signup on terabox.com automatically, but i keep having to solve captcha's which i cant do automatically without paying for something like 2captcha, or i find a repository where someone just left one

To install the dependecies just run the setup.py with python setup.py or python3 setup.py depending on what operating system you have.

Here are some example execution possibilties: 

python onionmail_creator.py --mode=tor --tor-socks=auto --browser=chrome --headless=true --stealth=true --accounts=1000 --concurrency=10

python onionmail_creator.py --mode=direct --browser=firefox --headless=False --stealth=True --accounts=30 --concurrency=2

You can also use proxies but i dont recommend doing that, because tor is just better for this. Out of 1000 accounts this script created about 990, and the other 10 failed, so the success rate is pretty high. 

It saves all the accounts in onionmail_accounts.txt like this username:password, you can extract it yourself or if i have written a script that depends on this you can run that one, because i will probably make it compatible with this.
