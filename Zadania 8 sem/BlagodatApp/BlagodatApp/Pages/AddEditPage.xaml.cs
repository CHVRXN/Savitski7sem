using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace WpfApp1.Pages
{
    /// <summary>
    /// Логика взаимодействия для AddEditPage.xaml
    /// </summary>
    public partial class AddEditPage : Page
    {

        Random _random = new Random();
        private int attemps = 0;
        TimeSpan duration;
        public AddEditPage()
        {
            InitializeComponent();
            Classes.DbConnect.modeldb = new Models.BlagodatEntities2();

            
            CanvasNoise.Visibility = Visibility.Collapsed;
            GetCapcha.Visibility = Visibility.Collapsed;
        }
        /// <summary>
        /// Логика Логика обновления капчи
        /// </summary>
        private void UpdateCaptcha()
        {
            Symbols = "";
            SPanelSymbols.Children.Clear();
            CanvasNoise.Children.Clear();



            GenerateSymbols(3);
            GenerateNoise(30);
        }

        public string Symbols = "";



        /// <summary>
        /// Логика генерации символов для капчи
        /// </summary>
        private void GenerateSymbols(int count)
        {
            string alphabet = "WERPASFHKXVBM234578";
            for (int i = 0; i < count; i++)
            {
                string symbol = alphabet.ElementAt(_random.Next(0, alphabet.Length)).ToString();
                TextBlock lbl = new TextBlock();



                lbl.Text = symbol;
                lbl.FontSize = _random.Next(20, 40);
                lbl.RenderTransform = new RotateTransform(_random.Next(-45, 45));
                lbl.Margin = new Thickness(20, 20, 20, 20);



                //lbl.Foreground = ra



                SPanelSymbols.Children.Add(lbl);

                Symbols = Symbols + symbol;
            }
        }


        /// <summary>
        /// Генерация шумов для капчи
        /// </summary>
        private void GenerateNoise(int volumeNoise)
        {
            for (int i = 0; i < volumeNoise; i++)
            {
                Ellipse ellipse = new Ellipse
                {
                    Fill = new SolidColorBrush(Color.FromArgb((byte)_random.Next(100, 200),
                   
                     (byte)_random.Next(0, 256),
                     (byte)_random.Next(0, 256),
                     (byte)_random.Next(0, 256)))
                };

                ellipse.Height = ellipse.Width = _random.Next(20, 60);

                Canvas.SetLeft(ellipse, _random.Next(0, 290));
                Canvas.SetTop(ellipse, _random.Next(0, 100));

                CanvasNoise.Children.Add(ellipse);
            }
        }
        private void CheckAttemps()
        {
            if (attemps == 2)
            {
                CanvasNoise.Visibility = Visibility.Visible;
                GetCapcha.Visibility = Visibility.Visible;
                CheckCaptcha.Visibility = Visibility.Visible;
                UpdateCaptcha();
                MessageBox.Show("Пройдите капчу.", "Не удается войти!", MessageBoxButton.OK, MessageBoxImage.Warning);

                if (GetCapcha.Text != Symbols)
                {
                    LoginUs.Visibility = Visibility.Hidden;
                    Password.Visibility = Visibility.Hidden;

                }
                else LoginUs.Visibility = Visibility.Visible;
            }
            else
            {
                if (attemps == 3)
                {
                    duration = TimeSpan.FromSeconds(10);

                    LoginTimerTB.Visibility = Visibility.Visible;
                   
                    BlockedTB.Text = "Превышено количество попыток авторизации.\nВозможность входа заблокирована.";
                    LoginUs.IsEnabled = false;
                }

            }
        }

        private void LogIN()
        {
            try
            {
                //Обратиться к таблице User, чтобы извлечь логин и пароль
                //var - общий тип
                //userObj - имя обьекта 
                //Информация об агенте - agentObj
                //папка, класс, модель, таблица
                //сравнить данные из таблицы и названия столбцов логин и пароль
                //Имена текстблоков с их функция текст и пароль
                //&& - И пользователь доллжен ввести и логин и пароль, иначе ошибка

                var userObj = Classes.DbConnect.modeldb.User.FirstOrDefault(x =>
                x.Login == LoginUs.Text && x.Password == Password.Password);

                /*if(LoginUs.Text=="test" && Password.Password=="test")
                {
                 //Manager.MainFrame.Navigate(new Administrator());
                }*/

                if (userObj != null )
                {
                    Models.BlagodatEntities2.currentuser = userObj;
                    MessageBox.Show("Здравствуйте " + userObj.Role.Title + ", " + userObj.Login, "Уведомление",
                        MessageBoxButton.OK, MessageBoxImage.Information);
                    switch (userObj.RoleID)
                    {
                        case 1:
                            NavigationService.Navigate(new ClientsPage());
                            break;
                        case 2:
                            NavigationService.Navigate(new Mangerrr());
                            break;
                        default:
                            MessageBox.Show("Данные не обнаружены!", "Уведомление", MessageBoxButton.OK, MessageBoxImage.Warning);
                            break;
                    }
                }
                else MessageBox.Show("Пользователя в БД нет", "Уведомление");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Ошибка: " + ex.Message.ToString(), "Критическая работа приложения",
                    MessageBoxButton.OK, MessageBoxImage.Warning);
            }
        }

        /// <summary>
        /// Обработка нажатия кнопки "Войти"
        /// </summary>
        private void Login(object sender, RoutedEventArgs e)
        {
            var userObj = Classes.DbConnect.modeldb.User.FirstOrDefault(x =>
                  x.Login == LoginUs.Text && x.Password == Password.Password);
            if (userObj == null)
            {
                MessageBox.Show("Такого пользователя нет!", "Ошибка при авторизации",
                    MessageBoxButton.OK, MessageBoxImage.Error);
                attemps++;
                CheckAttemps();

            }
            else
            {
                LogIN();
            }
        }
        /// <summary>
        /// Функция отвечает за возможность показать пароль
        /// </summary>
        private void TbxShowPass_MouseDown(object sender, MouseButtonEventArgs e)
        {
            TxbPassword.Visibility = Visibility.Visible;
            Password.Visibility = Visibility.Collapsed;
            TxbPassword.Text = Password.Password;
        }

        private void CheckCaptcha_Click(object sender, RoutedEventArgs e)
        {
            if (GetCapcha.Text == Symbols)
                LoginUs.Visibility = Visibility.Visible;
                Password.Visibility = Visibility.Visible;
        }
        /// <summary>
        /// Пароль скрывается
        /// </summary>
        private void TbxShowPass_MouseUp(object sender, MouseButtonEventArgs e)
        {
            TxbPassword.Visibility = Visibility.Collapsed;
            Password.Visibility = Visibility.Visible;
        }

        /// <summary>
        /// Обновление капчи
        /// </summary>
        private void BtnUpdateCaptcha_Click(object sender, RoutedEventArgs e)
        {
            UpdateCaptcha();
        }
        /// <summary>
        /// Обработка кнопки регистрации
        /// </summary>
        private void RegButton(object sender, RoutedEventArgs e)
        {
            NavigationService.Navigate(new RegPage());
        }
    }
}
