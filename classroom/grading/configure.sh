sudo sed -i "s/RHT_COURSE=.*/RHT_COURSE=bfx009/" /etc/rht
sudo sed -i "s/RHT_VERSION_LOCK=.*/RHT_VERSION_LOCK='>=9.0,<10.0'/" /etc/rht
sudo systemctl restart dynolabs-update.service
pip install pip install rht-labs-hol003==9.0.9.dev54 --extra-index-url https://pypi.apps.tools-na.prod.nextcle.com/repository/labs/simple/
lab select hol003
lab --version
source ~/.venv/labs/bin/activate
cd .venv/labs/lib/python3.9/site-packages/hol003/
#git pull https://github.com/YogiSoni-lazy/hol003.git
#git clone https://YogiSoni-lazy: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@github.com/YogiSoni-lazy/hol003.git
