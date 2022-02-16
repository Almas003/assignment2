# urls.py
from django.urls import path
from blockchain_analytics_charts.views import main_view

urlpatterns = [
    path("", main_view)
]



# views.py
from django.shortcuts import render
from .parser import get_balance_of_addresses

def main_view(request):
	balances = get_balance_of_addresses()
	return render(request, "index.html", {"balances": balances})


# etherscan.py
import requests

# Get Ether Balance for Multiple Addresses in a Single Call
url_sample = "https://api.etherscan.io/api?module=account&action=balancemulti&address=ADDRESSES&tag=latest&apikey=IZZ64IZCAP8MHKHJ1WJ8EK5UXN17S3PNI5"
addresses_file = open("../addresses.txt")
addresses = [address.replace("\n", "") for address in addresses_file.readlines()]
addresses_file.close()

def get_balance_for_multiple_addresses(addresses):
	r = requests.get(url_sample.replace("ADDRESSES", ",".join(addresses)))
	json = r.json()
	return json["result"]

def get_balance_of_addresses():
	result = []

	for i in range(0, 100, 20):
		print(i, i+20)
		for j in get_balance_for_multiple_addresses(addresses[i:i+20]):
			result.append(j)

	return result


# base.html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">

    <!-- Chart JS code -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.0.2/dist/chart.min.js"></script>

    <title>Blockchain analytics charts</title>
  </head>
  <body>
    <div class="container">

        {% block content %}

        {% endblock %}

    </div>
  </body>
</html>



# index.html
{% extends 'base.html' %}


{% block content %}
<div class="col-md-8" style="width: 100%;">
    <canvas id="chart_bar"></canvas> <!--  width="400" height="250" -->
        <script>
        var ctx = document.getElementById('chart_bar').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: [{% for balance in balances %}  '{{ balance.account }}',  {% endfor %}],
                datasets: [{
                    label: 'Balance',
                    data: [{% for balance in balances %}  {{ balance.balance }},  {% endfor %}],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.8)',
                        'rgba(54, 162, 235, 0.8)',
                        'rgba(255, 206, 86, 0.8)',
                        'rgba(75, 192, 192, 0.8)',
                        'rgba(153, 102, 255, 0.8)',
                        'rgba(255, 159, 64, 0.8)',
                        'rgba(240, 120, 50, 0.8)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(240, 120, 50, 1)',

                    ],
                    borderWidth: 2
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
        </script>
</div>

<div class="col-md-8" style="width: 100%;">
    <canvas id="chart_pie"></canvas> <!--  width="400" height="250" -->
        <script>
        var ctx = document.getElementById('chart_pie').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: [{% for balance in balances %}  '{{ balance.account }}',  {% endfor %}],
                datasets: [{
                    label: '# of Balance',
                    data: [{% for balance in balances %}  {{ balance.balance }},  {% endfor %}],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.8)',
                        'rgba(54, 162, 235, 0.8)',
                        'rgba(255, 206, 86, 0.8)',
                        'rgba(75, 192, 192, 0.8)',
                        'rgba(153, 102, 255, 0.8)',
                        'rgba(255, 159, 64, 0.8)',
                        'rgba(240, 120, 50, 0.8)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(240, 120, 50, 1)',

                    ],
                    borderWidth: 2
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
        </script>
</div>

<div class="col-md-8" style="width: 100%;">
    <canvas id="chart_line"></canvas> <!--  width="400" height="250" -->
        <script>
        var ctx = document.getElementById('chart_line').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [{% for balance in balances %}  '{{ balance.account }}',  {% endfor %}],
                datasets: [{
                    label: '# of Balance',
                    data: [{% for balance in balances %}  {{ balance.balance }},  {% endfor %}],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.8)',
                        'rgba(54, 162, 235, 0.8)',
                        'rgba(255, 206, 86, 0.8)',
                        'rgba(75, 192, 192, 0.8)',
                        'rgba(153, 102, 255, 0.8)',
                        'rgba(255, 159, 64, 0.8)',
                        'rgba(240, 120, 50, 0.8)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(240, 120, 50, 1)',

                    ],
                    borderWidth: 2
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
        </script>
</div>
{% endblock %}




# addresses.txt
0x00000000219ab540356cbb839cbe05303d7705fa
0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
0xda9dfa130df4de4673b89022ee50ff26f6ea73cf
0x73bceb1cd57c711feac4224d062b0f6ff338501e
0xbe0eb53f46cd790cd13851d5eff43d12404d33e8
0x9bf4001d307dfd62b26a2f1307ee0c0307632d59
0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5
0x61edcdf5bb737adffe5043706e7c5bb1f1a56eea
0xdc24316b9ae028f1497c275eb9192a3ea0f67022
0x1b3cb81e51011b549d78bf720b0d924ac763a7c2
0x011b6e24ffb0b5f5fcc564cf4183c5bbbc96d515
0x07ee55aa48bb72dcc6e9d78256648910de513eca
0xc61b9bb3a7a0767e3179713f3a5c7a9aedce193c
0x8484ef722627bf18ca5ae6bcf031c23e6e922b30
0xe92d1a43df510f82c66382592a047d288f85226f
0x742d35cc6634c0532925a3b844bc454e4438f44e
0xf977814e90da44bfa03b6295a0616a897441acec
0xdf9eb223bafbe5c5271415c75aecd68c21fe3d7f
0x0548f59fee79f8832c299e01dca5c76f034f558e
0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
0xa929022c9107643515f5c777ce9a910f0d1e490c
0x220866b1a2219f40e72f5c628b65d54268ca3a9d
0xca8fa8f0b631ecdb18cda619c4fc9d197c8affca
0x6262998ced04146fa42253a5c0af90ca02dfd2a3
0x176f3dab24a159341c0509bb36b833e7fdd0a132
0x3bfc20f0b9afcace800d73d2191166ff16540258
0xa7efae728d2936e78bda97dc267687568dd593f3
0x8103683202aa8da10536036edef04cdd865c225e
0x0a4c79ce84202b03e95b7a692e5d728d83c44c76
0x7d24796f7ddb17d73e8b1d0a3bbd103fba2cb2fe
0x2b6ed29a95753c3ad948348e3e7b1a251080ffb9
0xbddf00563c9abd25b576017f08c46982012f12be
0x189b9cbd4aff470af2c0102f365fc1823d857965
0x9845e1909dca337944a0272f1f9f7249833d2d19
0x2faf487a4414fe77e2327f0bf4ae2a264a776ad2
0x59448fe20378357f206880c58068f095ae63d5a5
0x0c23fc0ef06716d2f8ba19bc4bed56d045581f2d
0x66f820a414680b5bcda5eeca5dea238543f42054
0xb29380ffc20696729b7ab8d093fa1e2ec14dfe2b
0x558553d54183a8542f7832742e7b4ba9c33aa1e6
0x98ec059dc3adfbdd63429454aeb0c990fba4a128
0xcdbf58a9a9b54a2c43800c50c7192946de858321
0x19184ab45c40c2920b0e0e31413b9434abd243ed
0x90a9e09501b70570f9b11df2a6d4f047f8630d6d
0xbf3aeb96e164ae67e763d9e050ff124e7c3fdd28
0xb8808f9e9b88497ec522304055cd537a0913f6a0
0xf774da4418c6dca3051f0e7570829b24214e730b
0x1db92e2eebc8e0c075a02bea49a2935bcd2dfcf4
0xdc1487e092caba080c6badafaa75a58ce7a2ec34
0x36a85757645e8e8aec062a1dee289c7d615901ca
0xef22c14f46858d5ac61326497b056974167f2ee1
0xd69b0089d9ca950640f5dc9931a41a5965f00303
0xa7e4fecddc20d83f36971b67e13f1abc98dfcfa6
0x7da82c7ab4771ff031b66538d2fb9b0b047f6cf9
0x5b5b69f4e0add2df5d2176d7dbd20b4897bc7ec4
0x78605df79524164911c144801f41e9811b7db73d
0x28c6c06298d514db089934071355e5743bf21d60
0x3ba25081d3935fcc6788e6220abcace39d58d95d
0xfd898a0f677e97a9031654fc79a27cb5e31da34a
0x701c484bfb40ac628afa487b6082f084b14af0bd
0x4b4a011c420b91260a272afd91e54accdafdfc1d
0xa8dcc0373822b94d7f57326be24ca67bafcaad6b
0x367989c660881e1ca693730f7126fe0ffc0963fb
0x0ff64c53d295533a37f913bb78be9e2adc78f5fe
0x844ada2ed8ecd77a1a9c72912df0fcb8b8c495a7
0x9c2fc4fc75fa2d7eb5ba9147fa7430756654faa9
0xb20411c403687d1036e05c8a7310a0f218429503
0x9a1ed80ebc9936cee2d3db944ee6bd8d407e7f9f
0xb8cda067fabedd1bb6c11c626862d7255a2414fe
0xb9fa6e54025b4f0829d8e1b42e8b846914659632
0xba18ded5e0d604a86428282964ae0bb249ceb9d0
0xfe01a216234f79cfc3bea7513e457c6a9e50250d
0x0c05ec4db907cfb91b2a1a29e7b86688b7568a6d
0xc4cf565a5d25ee2803c9b8e91fc3d7c62e79fe69
0xe04cf52e9fafa3d9bf14c407afff94165ef835f7
0x77afe94859163abf0b90725d69e904ea91446c7b
0x19d599012788b991ff542f31208bab21ea38403e
0xca582d9655a50e6512045740deb0de3a7ee5281f
0xd05e6bf1a00b5b4c9df909309f19e29af792422b
0x0f00294c6e4c30d9ffc0557fec6c586e6f8c3935
0xeb2b00042ce4522ce2d1aacee6f312d26c4eb9d6
0x7ae92148e79d60a0749fd6de374c8e81dfddf792
0x554f4476825293d4ad20e02b54aca13956acc40a
0x9cf36e93a8e2b1eaaa779d9965f46c90b820048c
0x4756eeebf378046f8dd3cb6fa908d93bfd45f139
0x091933ee1088cdf5daace8baec0997a4e93f0dd6
0xa0efb63be0db8fc11681a598bf351a42a6ff50e0
0x8b83b9c4683aa4ec897c569010f09c6d04608163
0x550cd530bc893fc6d2b4df6bea587f17142ab64e
0x828103b231b39fffce028562412b3c04a4640e64
0xe35b0ef92452c353dbb93775e0df97cedf873c72
0x0518f5bb058f6215a0ff5f4df54dae832d734e04
0x0e86733eab26cfcc04bb1752a62ec88e910b4cf5
0xb8b6fe7f357adeab950ac6c270ce340a46989ce1
0xeddf8eb4984cc27407a568cae1c78a1ddb0c2c1b
0x7145cfedcf479bede20c0a4ba1868c93507d5786
0x2fa9f9efc767650aace0422668444c3ff63e1f8d
0xa160cdab225685da1d56aa342ad8841c3b53f291
0xd57479b8287666b44978255f1677e412d454d4f0
0x4baf012726cb5ec7dda57bc2770798a38100c44d
0x71c7656ec7ab88b098defb751b7401b5f6d8976f