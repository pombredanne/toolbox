import re

html = '''
<div class="sp-palette sp-thumb sp-cf"><div class="sp-cf sp-palette-row sp-palette-row-0"><span title="#a47462" data-color="rgb(164, 116, 98)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(164, 116, 98);"></span></span><span title="#c2726a" data-color="rgb(194, 114, 106)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(194, 114, 106);"></span></span><span title="#e4523d" data-color="rgb(228, 82, 61)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(228, 82, 61);"></span></span><span title="#e7664d" data-color="rgb(231, 102, 77)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(231, 102, 77);"></span></span><span title="#ee7e4a" data-color="rgb(238, 126, 74)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(238, 126, 74);"></span></span><span title="#f4ae55" data-color="rgb(244, 174, 85)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(244, 174, 85);"></span></span></div><div class="sp-cf sp-palette-row sp-palette-row-1"><span title="#76ce90" data-color="rgb(118, 206, 144)" class="sp-thumb-el sp-thumb-light sp-thumb-active"><span class="sp-thumb-inner" style="background-color:rgb(118, 206, 144);"></span></span><span title="#53a063" data-color="rgb(83, 160, 99)" class="sp-thumb-el sp-thumb-dark"><span class="sp-thumb-inner" style="background-color:rgb(83, 160, 99);"></span></span><span title="#94c849" data-color="rgb(148, 200, 73)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(148, 200, 73);"></span></span><span title="#bfd56f" data-color="rgb(191, 213, 111)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(191, 213, 111);"></span></span><span title="#fae589" data-color="rgb(250, 229, 137)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(250, 229, 137);"></span></span><span title="#f5ce6e" data-color="rgb(245, 206, 110)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(245, 206, 110);"></span></span></div><div class="sp-cf sp-palette-row sp-palette-row-2"><span title="#a6dcbf" data-color="rgb(166, 220, 191)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(166, 220, 191);"></span></span><span title="#addfe5" data-color="rgb(173, 223, 229)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(173, 223, 229);"></span></span><span title="#a6c7e5" data-color="rgb(166, 199, 229)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(166, 199, 229);"></span></span><span title="#4f8de4" data-color="rgb(79, 141, 228)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(79, 141, 228);"></span></span><span title="#95a5fd" data-color="rgb(149, 165, 253)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(149, 165, 253);"></span></span><span title="#b0a5fd" data-color="rgb(176, 165, 253)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(176, 165, 253);"></span></span></div><div class="sp-cf sp-palette-row sp-palette-row-3"><span title="#c2c2c2" data-color="rgb(194, 194, 194)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(194, 194, 194);"></span></span><span title="#c8bebf" data-color="rgb(200, 190, 191)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(200, 190, 191);"></span></span><span title="#c6a8ad" data-color="rgb(198, 168, 173)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(198, 168, 173);"></span></span><span title="#e79ab5" data-color="rgb(231, 154, 181)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(231, 154, 181);"></span></span><span title="#bd86e5" data-color="rgb(189, 134, 229)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(189, 134, 229);"></span></span><span title="#9987e1" data-color="rgb(153, 135, 225)" class="sp-thumb-el sp-thumb-light"><span class="sp-thumb-inner" style="background-color:rgb(153, 135, 225);"></span></span></div><div class="sp-cf sp-palette-row sp-palette-row-selection"></div></div>
'''

m = re.findall('title="#(.*?)"', html)

print(m)

''' result '''
'a47462', 'c2726a', 'e4523d', 'e7664d', 'ee7e4a', 'f4ae55', '76ce90', '53a063', '94c849', 'bfd56f', 'fae589', 'f5ce6e', 'a6dcbf', 'addfe5', 'a6c7e5', '4f8de4', '95a5fd', 'b0a5fd', 'c2c2c2', 'c8bebf', 'c6a8ad', 'e79ab5', 'bd86e5', '9987e1'