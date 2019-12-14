
CREATE TABLE `product_category` (
  `category_title` varchar(50) NOT NULL primary key,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `product_category` (`category_title`, `created_date`) VALUES
('clothing', '2019-11-05 15:16:46'),
('electronics', '2019-11-05 15:16:46'),
('decoration', '2019-11-10 05:02:20'),
('home', '2019-11-10 05:02:20');



CREATE TABLE `product_sub_category` (
  `category_title` varchar(50) NOT NULL,
  `sub_category_title` varchar(50) NOT NULL primary key,
  `created date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  FOREIGN KEY (`category_title`) REFERENCES `product_category` (`category_title`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `product_sub_category` (`category_title`, `sub_category_title`, `created date`) VALUES
('clothing', 'mobiles', '2019-11-05 15:21:22'),
('clothing', 'televisions', '2019-11-05 15:21:22'),
('electronics', 'formals', '2019-11-10 05:04:34'),
('electronics', 'casual', '2019-11-10 05:04:34'),
('decoration', 'outdoor', '2019-11-10 05:05:00'),
('decoration', 'indoor', '2019-11-10 05:05:00'),
('home', 'kitchen', '2019-11-10 05:05:30'),
('home', 'living', '2019-11-10 05:05:30');

CREATE TABLE `product_child_category` (
  `category_title` varchar(50) NOT NULL,
  `sub_category_title` varchar(50) NOT NULL,
  `child_category_title` varchar(20) NOT NULL primary key,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  FOREIGN KEY (`category_title`) REFERENCES `product_category` (`category_title`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`sub_category_title`) REFERENCES `product_sub_category` (`sub_category_title`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `product_child_category` (`category_title`, `sub_category_title`, `child_category_title`, `created_date`) VALUES
('electronics', 'mobiles', 'Vivo phone', '2019-11-05 15:23:01'),
('electronics', 'mobiles', 'appo phone', '2019-11-05 15:23:01'),
('electronics', 'televisions', 'LG full HD TV', '2019-11-05 15:24:40'),
('electronics', 'televisions', 'Mi Tv', '2019-11-05 15:24:40');







