const goods = [
  { title: 'Shirt', price: 150, sale: 25},
  { title: 'Socks', price: 50, sale: 25},
  { title: 'Jacket', price: 350},
  { title: 'Shoes', price: 250},
];

const renderGoodsItem = ({title = "product", price = 0, sale = 10, button = "Купить"}) => {
  return `
  <div class="goods-item">
      <h3>${title}</h3>
      <p>${price}</p>
      <div class="badge">${sale}%</div>
      <button class="btn btn-outline-primary btn-sm">${button}</button>
    </div>
  `;
};

const [{title, price, sale, button}] = goods;

const renderGoodsList = (list) => {
  let goodsList = list.map(item => renderGoodsItem(item));
  document.querySelector('.goods-list').innerHTML = goodsList.join('');
}

renderGoodsList(goods);