// just wanna use this to get back into the swing of javascript after a year of python. going to write some basic functons for

// function to add 2 numbers

function add_numbers(x, y) {
  return x + y;
}

// find the maximum value in an array

function find_maximum(arr) {
  var maximum = 0;
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] > maximum) {
      maximum = arr[i];
    }
  }
  return maximum;
}

// or

function max(arr) {
  var maximum = math.max(arr);
  return maximum
}

// return every item in an array that appears 3 times or more
//uses map obeject

function find_triples(arr) {
  var value_counts = new Map();
  var final_array = [];
  for (var i = 0; i < arr.length; i++) {
    if (value_counts.has(arr[i])) {
      value_counts.set(arr[i], value_counts.get(arr[i]) + 1);
    }
    else {
      value_counts.set(arr[i], 1)
    }
  }
  for (var [key, value] of value_counts) {
    if (value > 2){
      final_array.push(key);
    }
  }
  console.log(value_counts)
  return final_array
}