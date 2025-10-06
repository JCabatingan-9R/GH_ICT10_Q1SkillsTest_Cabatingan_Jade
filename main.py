from pyscript import display, document


def orderoutput(e):
    # remove repeat
    document.querySelector("#output").innerText = ""

    # variables for orderer information
    firstname = document.getElementById('fname').value
    lastname = document.getElementById('lname').value
    address = document.getElementById('address').value
    phone = document.getElementById('number').value

    # get id of checkboxes
    svt = document.getElementById('svtls')
    enha = document.getElementById('enls')
    bnd = document.getElementById('bndls')
    ive = document.getElementById('ivels')
    skz = document.getElementById('skzls')

    # get value of checkboxes
    svt1 = document.getElementById('svtls').value
    enha1 = document.getElementById('enls').value
    bnd1 = document.getElementById('bndls').value
    ive1 = document.getElementById('ivels').value
    skz1 = document.getElementById('skzls').value

    # total for order/s
    total = float(svt1) * svt.checked + float(enha1) * enha.checked + float(bnd1) * bnd.checked + float(ive1) * ive.checked + float(skz1) * skz.checked

    # multisting for orderer information output
    multi = f"""
    Order for: {firstname} {lastname}
    Address: {address}
    Contact Number: {phone}
    Total: Php {total:.2f}
    """

    # displaying information to output
    display(multi, target='output')
