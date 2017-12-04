function setname(name, entry_id){
    document.getElementById('lable_name').innerHTML = name.toString();
    href_str = document.getElementById('delete_submit').href;
    var split = href_str.split('/');
    var new_str = "";
    split[split.length-2] = entry_id.toString();
    for(var i=0; i<split.length; i++){
        new_str += split[i];
        if(i != split.length-1) {
            new_str += '/';
        }
    }
    document.getElementById('delete_submit').href = new_str;
}
