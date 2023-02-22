use std::mem::size_of_val;

const PI:f32 = 3.14;

fn main() {

    println!("PI : {}",PI);

    let vari: i32 = 127;
    println!("Number : {} -- Size : {} bytes", vari, size_of_val(&vari));

    let varw: char = 'a';
    println!("Char : {} -- Size : {} bytes",varw,size_of_val(&varw));

    let varb: bool = true;
    println!("Bool : {} -- Size : {} bytes",varb,size_of_val(&varb));

    let mut var_mutable: u16 = 300;
    println!("Char : {} -- Size : {} bytes",var_mutable,size_of_val(&var_mutable));
}