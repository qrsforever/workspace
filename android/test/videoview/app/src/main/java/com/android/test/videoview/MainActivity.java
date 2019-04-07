package com.android.test.videoview;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;
import java.util.UUID;
import java.io.OutputStream;
import java.io.IOException;

import android.util.Log;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Context;
import android.content.res.Configuration;
import android.media.AudioManager;
import android.media.MediaPlayer;
import android.media.MediaPlayer.OnCompletionListener;
import android.media.MediaPlayer.OnPreparedListener;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.View.OnTouchListener;
import android.view.animation.Animation;
import android.view.animation.Animation.AnimationListener;
import android.view.animation.AnimationUtils;
import android.view.Gravity;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.SeekBar.OnSeekBarChangeListener;
import android.widget.TextView;
import android.widget.Toast;
import android.os.Environment;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.BroadcastReceiver;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;

public class MainActivity extends Activity implements OnClickListener {

	final static String TAG = "QRS-MainActivity";

    private static final int REQUEST_DISCOVERY = 0x1;
	private FullScreenVideoView mVideo;
	private View mTopView;
	private View mBottomView;
	private SeekBar mSeekBar;
	private ImageView mPlay;
	private TextView mPlayTime;
	private TextView mDurationTime;

	// 音频管理器
	private AudioManager mAudioManager;

	// 屏幕宽高
	private float mWidth;
	private float mHeight;

	// 视频播放时间
	private int playTime;

    private String videoUrl = "";

	// 自动隐藏顶部和底部View的时间
	private static final int HIDE_TIME = 5000;

	// 声音调节Toast
	private VolumnController volumnController;

    // 建立蓝牙通信的UUID
    // private static final UUID mUuid = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
    // 自带的蓝牙适配器
    // private BluetoothAdapter mBluetoothAdapter = null;
    // 扫描得到的蓝牙设备
    // private BluetoothDevice mDevice = null;
    // 蓝牙通信socket
    // private BluetoothSocket mBtSocket = null;
    // 手机输出流
    // private OutputStream mOutStream = null;
    // public static BluetoothReceiver mReceiver;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);

        // 视频路径: res/raw/seabird.mp4
        videoUrl = "android.resource://" + getPackageName() + "/" + R.raw.seabird;
		setContentView(R.layout.activity_main);
		volumnController = new VolumnController(this);
		mVideo = (FullScreenVideoView) findViewById(R.id.videoview);
		mPlayTime = (TextView) findViewById(R.id.play_time);
		mDurationTime = (TextView) findViewById(R.id.total_time);
		mPlay = (ImageView) findViewById(R.id.play_btn);
		mSeekBar = (SeekBar) findViewById(R.id.seekbar);
		mTopView = findViewById(R.id.top_layout);
		mBottomView = findViewById(R.id.bottom_layout);

		mAudioManager = (AudioManager) getSystemService(Context.AUDIO_SERVICE);

		mWidth = DensityUtil.getWidthInPx(this);
		mHeight = DensityUtil.getHeightInPx(this);
		threshold = DensityUtil.dip2px(this, 18);

		mPlay.setOnClickListener(this);
		mSeekBar.setOnSeekBarChangeListener(mSeekBarChangeListener);

        // mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        // bluetoothAction();
        // connectToDevice();
        playVideo();
	}


    // public void bluetoothAction() {
    //     if (mBluetoothAdapter != null) {
    //         if (!mBluetoothAdapter.isEnabled()) {
    //             Log.d(TAG, "enable blue");
    //             mBluetoothAdapter.enable();

    //             mBluetoothAdapter.startDiscovery();
    //             IntentFilter filter = new IntentFilter(BluetoothDevice.ACTION_FOUND);
    //             mReceiver = new BluetoothReceiver();
    //             registerReceiver(mReceiver, filter);
    //         }
    //     } else
    //         this.finish();
    // }

    // public void connectToDevice() {
    //     if (mBluetoothAdapter.isEnabled()) {
    //         Intent intent = new Intent(this, DiscoveryActivity.class);
    //         displayLongToast("请选择一个蓝牙设备进行连接！");
    //         this.startActivityForResult(intent, REQUEST_DISCOVERY);
    //     } else {
    //         this.finish();
    //     }
    // }

    // private class BluetoothReceiver extends BroadcastReceiver {

    //     @Override
    //     public void onReceive(Context context, Intent intent) {
    //     } 
    // }

    // @Override
    // protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    //     Log.d(TAG, "onActivityResult(" + requestCode + ", " + resultCode + ")");
    //     if (requestCode != REQUEST_DISCOVERY) {
    //         return;
    //     }
    //     if (resultCode != RESULT_OK) {
    //         return;
    //     }

    //     String addressStr = data.getStringExtra("address");
    //     mDevice = mBluetoothAdapter.getRemoteDevice(addressStr);
    //     try {
    //         mBtSocket = mDevice.createRfcommSocketToServiceRecord(mUuid);
    //     } catch (Exception e) {
    //         displayLongToast("通信通道创建失败！");
    //     }

    //     if (mBtSocket != null) {
    //         try {
    //             mBtSocket.connect();
    //             displayLongToast("通信通道连接成功！");
    //         } catch (IOException ioe) {
    //             displayLongToast("通信通道连接失败！");
    //             try {
    //                 mBtSocket.close();
    //                 displayLongToast("通信通道已关闭！");
    //             } catch (IOException ioe2) {
    //                 displayLongToast("通信通道尚未连接，无法关闭！");
    //             }
    //         }
    //         try {
    //             mOutStream = mBtSocket.getOutputStream();
    //         } catch (IOException e) {
    //             displayLongToast("数据流创建失败！");
    //         }
    //     }
    // }


	@Override
	public void onConfigurationChanged(Configuration newConfig) {
		if (this.getResources().getConfiguration().orientation == Configuration.ORIENTATION_LANDSCAPE) {
			mHeight = DensityUtil.getWidthInPx(this);
			mWidth = DensityUtil.getHeightInPx(this);
		} else if (this.getResources().getConfiguration().orientation == Configuration.ORIENTATION_PORTRAIT) {
			mWidth = DensityUtil.getWidthInPx(this);
			mHeight = DensityUtil.getHeightInPx(this);
		}
		super.onConfigurationChanged(newConfig);
	}

	@Override
	protected void onPause() {
		super.onPause();
	}

	private OnSeekBarChangeListener mSeekBarChangeListener = new OnSeekBarChangeListener() {

		@Override
		public void onStopTrackingTouch(SeekBar seekBar) {
			mHandler.postDelayed(hideRunnable, HIDE_TIME);
		}

		@Override
		public void onStartTrackingTouch(SeekBar seekBar) {
			mHandler.removeCallbacks(hideRunnable);
		}

		@Override
		public void onProgressChanged(SeekBar seekBar, int progress,
				boolean fromUser) {
			if (fromUser) {
				int time = progress * mVideo.getDuration() / 100;
				mVideo.seekTo(time);
			}
		}
	};

	private void backward(float delataX) {
		int current = mVideo.getCurrentPosition();
		int backwardTime = (int) (delataX / mWidth * mVideo.getDuration());
		int currentTime = current - backwardTime;
		mVideo.seekTo(currentTime);
		mSeekBar.setProgress(currentTime * 100 / mVideo.getDuration());
		mPlayTime.setText(formatTime(currentTime));
	}

	private void forward(float delataX) {
		int current = mVideo.getCurrentPosition();
		int forwardTime = (int) (delataX / mWidth * mVideo.getDuration());
		int currentTime = current + forwardTime;
		mVideo.seekTo(currentTime);
		mSeekBar.setProgress(currentTime * 100 / mVideo.getDuration());
		mPlayTime.setText(formatTime(currentTime));
	}

	private void volumeDown(float delatY) {
		int max = mAudioManager.getStreamMaxVolume(AudioManager.STREAM_MUSIC);
		int current = mAudioManager.getStreamVolume(AudioManager.STREAM_MUSIC);
		int down = (int) (delatY / mHeight * max * 3);
		int volume = Math.max(current - down, 0);
		mAudioManager.setStreamVolume(AudioManager.STREAM_MUSIC, volume, 0);
		int transformatVolume = volume * 100 / max;
		volumnController.show(transformatVolume);
	}

	private void volumeUp(float delatY) {
		int max = mAudioManager.getStreamMaxVolume(AudioManager.STREAM_MUSIC);
		int current = mAudioManager.getStreamVolume(AudioManager.STREAM_MUSIC);
		int up = (int) ((delatY / mHeight) * max * 3);
		int volume = Math.min(current + up, max);
		mAudioManager.setStreamVolume(AudioManager.STREAM_MUSIC, volume, 0);
		int transformatVolume = volume * 100 / max;
		volumnController.show(transformatVolume);
	}

	@Override
	protected void onDestroy() {
		super.onDestroy();
		mHandler.removeMessages(0);
		mHandler.removeCallbacksAndMessages(null);
	}

	@SuppressLint("HandlerLeak")
	private Handler mHandler = new Handler() {

		@Override
		public void handleMessage(Message msg) {
			super.handleMessage(msg);
			switch (msg.what) {
			case 1:
				if (mVideo.getCurrentPosition() > 0) {
					mPlayTime.setText(formatTime(mVideo.getCurrentPosition()));
					int progress = mVideo.getCurrentPosition() * 100 / mVideo.getDuration();
					mSeekBar.setProgress(progress);
					if (mVideo.getCurrentPosition() > mVideo.getDuration() - 100) {
						mPlayTime.setText("00:00");
						mSeekBar.setProgress(0);
					}
					mSeekBar.setSecondaryProgress(mVideo.getBufferPercentage());
				} else {
					mPlayTime.setText("00:00");
					mSeekBar.setProgress(0);
				}

				break;
			case 2:
				showOrHide();
				break;

			default:
				break;
			}
		}
	};

	private void playVideo() {
		mVideo.setVideoPath(videoUrl);
		mVideo.requestFocus();
        mVideo.seekTo(1);
		mVideo.setOnPreparedListener(new OnPreparedListener() {
			@Override
			public void onPrepared(MediaPlayer mp) {
				mVideo.setVideoWidth(mp.getVideoWidth());
				mVideo.setVideoHeight(mp.getVideoHeight());

				// mVideo.start();
				if (playTime != 0) {
					mVideo.seekTo(playTime);
				}

				mHandler.removeCallbacks(hideRunnable);
				mHandler.postDelayed(hideRunnable, HIDE_TIME);
				mDurationTime.setText(formatTime(mVideo.getDuration()));
				Timer timer = new Timer();
				timer.schedule(new TimerTask() {

					@Override
					public void run() {
						mHandler.sendEmptyMessage(1);
					}
				}, 0, 1000);
			}
		});
		mVideo.setOnCompletionListener(new OnCompletionListener() {
			@Override
			public void onCompletion(MediaPlayer mp) {
				mPlay.setImageResource(R.drawable.video_btn_down);
				mPlayTime.setText("00:00");
				mSeekBar.setProgress(0);
                mVideo.seekTo(1);
			}
		});
		mVideo.setOnTouchListener(mTouchListener);
	}

	private Runnable hideRunnable = new Runnable() {

		@Override
		public void run() {
			showOrHide();
		}
	};

	@SuppressLint("SimpleDateFormat")
	private String formatTime(long time) {
		DateFormat formatter = new SimpleDateFormat("mm:ss");
		return formatter.format(new Date(time));
	}

	private float mLastMotionX;
	private float mLastMotionY;
	private int startX;
	private int startY;
	private int threshold;
	private boolean isClick = true;

	private OnTouchListener mTouchListener = new OnTouchListener() {

		@Override
		public boolean onTouch(View v, MotionEvent event) {
			final float x = event.getX();
			final float y = event.getY();

			switch (event.getAction()) {
			case MotionEvent.ACTION_DOWN:
				mLastMotionX = x;
				mLastMotionY = y;
				startX = (int) x;
				startY = (int) y;
				break;
			case MotionEvent.ACTION_MOVE:
				float deltaX = x - mLastMotionX;
				float deltaY = y - mLastMotionY;
				float absDeltaX = Math.abs(deltaX);
				float absDeltaY = Math.abs(deltaY);
				// 声音调节标识
				boolean isAdjustAudio = false;
				if (absDeltaX > threshold && absDeltaY > threshold) {
					if (absDeltaX < absDeltaY) {
						isAdjustAudio = true;
					} else {
						isAdjustAudio = false;
					}
				} else if (absDeltaX < threshold && absDeltaY > threshold) {
					isAdjustAudio = true;
				} else if (absDeltaX > threshold && absDeltaY < threshold) {
					isAdjustAudio = false;
				} else {
					return true;
				}
				if (isAdjustAudio) {
                    if (deltaY > 0) {
                        volumeDown(absDeltaY);
                    } else if (deltaY < 0) {
                        volumeUp(absDeltaY);
                    }
				} else {
					if (deltaX > 0) {
						forward(absDeltaX);
					} else if (deltaX < 0) {
						backward(absDeltaX);
					}
				}
				mLastMotionX = x;
				mLastMotionY = y;
				break;
			case MotionEvent.ACTION_UP:
				if (Math.abs(x - startX) > threshold
						|| Math.abs(y - startY) > threshold) {
					isClick = false;
				}
				mLastMotionX = 0;
				mLastMotionY = 0;
				startX = (int) 0;
				if (isClick) {
					showOrHide();
				}
				isClick = true;
				break;

			default:
				break;
			}
			return true;
		}

	};

	@Override
	public void onClick(View v) {
		switch (v.getId()) {
		case R.id.play_btn:
			if (mVideo.isPlaying()) {
				mVideo.pause();
				mPlay.setImageResource(R.drawable.video_btn_down);
			} else {
				mVideo.start();
				mPlay.setImageResource(R.drawable.video_btn_on);
			}
			break;
		default:
			break;
		}
	}

	private void showOrHide() {
		if (mTopView.getVisibility() == View.VISIBLE) {
			mTopView.clearAnimation();
			Animation animation = AnimationUtils.loadAnimation(this,
					R.anim.option_leave_from_top);
			animation.setAnimationListener(new AnimationImp() {
				@Override
				public void onAnimationEnd(Animation animation) {
					super.onAnimationEnd(animation);
					mTopView.setVisibility(View.GONE);
				}
			});
			mTopView.startAnimation(animation);

			mBottomView.clearAnimation();
			Animation animation1 = AnimationUtils.loadAnimation(this,
					R.anim.option_leave_from_bottom);
			animation1.setAnimationListener(new AnimationImp() {
				@Override
				public void onAnimationEnd(Animation animation) {
					super.onAnimationEnd(animation);
					mBottomView.setVisibility(View.GONE);
				}
			});
			mBottomView.startAnimation(animation1);
		} else {
			mTopView.setVisibility(View.VISIBLE);
			mTopView.clearAnimation();
			Animation animation = AnimationUtils.loadAnimation(this,
					R.anim.option_entry_from_top);
			mTopView.startAnimation(animation);

			mBottomView.setVisibility(View.VISIBLE);
			mBottomView.clearAnimation();
			Animation animation1 = AnimationUtils.loadAnimation(this,
					R.anim.option_entry_from_bottom);
			mBottomView.startAnimation(animation1);
			mHandler.removeCallbacks(hideRunnable);
			mHandler.postDelayed(hideRunnable, HIDE_TIME);
		}
	}

	private class AnimationImp implements AnimationListener {

		@Override
		public void onAnimationEnd(Animation animation) {

		}

		@Override
		public void onAnimationRepeat(Animation animation) {
		}

		@Override
		public void onAnimationStart(Animation animation) {
		}

	}

    public void displayLongToast(String str) {
        Toast toast = Toast.makeText(this, str, Toast.LENGTH_LONG);
        toast.setGravity(Gravity.TOP, 0, (int)(mHeight/2));
        toast.show();
        Log.d(TAG, str);
    }

    public void displayShortToast(String str) {
        Toast toast = Toast.makeText(this, str, Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, (int)(mHeight/2));
        toast.show();
        Log.d(TAG, str);
    }
}
