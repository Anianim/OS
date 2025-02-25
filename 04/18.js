// 객체와 레퍼런스 카운트에 대한 예시

// players 객체 생성
let players = {
    boys : {
        Bergkamp : "Striker"
    }
}
// persons 변수에 players 객체를 할당
let persons = players


// players 변수에 새로운 배열을 할당
players = ["Son", "Park"]

// human 변수에 persons 객체의 boys 속성을 할당
let human = persons.boys

// persons 변수에 새로운 문자열을 할당
persons = "persons"
