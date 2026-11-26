# A paid moving-height comparison for the attached type-four cap

Research deduction, 7 November 2026. On the actual coupled attached
height \(-.078<c<-.020\), the complete first-type-four cap envelope
and its adjoining central or real-cut profile increase with slope
greater than \(1/300\) under the affine early first-height change.
The ordinary contour height is fixed and nonpositive, and the next
retained target is held fixed.

This uses an ordinary second vertex and the attached-height
compatibility theorem for length at least three. It makes no
length-two claim. The high physical-tail alternatives and the
neighboring-height contribution remain separate.

## 1. Actual source and the remaining derivative

Use the literal source and allocations of the
[complete adjoining envelope](research_mixed_first_attached_complete_contour_envelope.md),
the exact reductions of the
[moving-height note](research_mixed_first_attached_moving_height_reduction.md),
and the [raised-index barrier](research_mixed_first_attached_index_barrier.md).
The first cap has type four. Its actual attached reference satisfies
\[
                         -.078<c<-.020.                         \tag{1}
\]
For an ordinary-ended open word this is Theorem 1 of the
[coupled attached-height deduction](research_mixed_first_four_attached_height_bound.md),
with an ordinary second vertex. The same saved compatibility argument
applies to an actual four-ending Fourier prefix of length \(m\ge3\):
\[
 a_*=E_4(b_*),\qquad B_\epsilon(a_*,c_*)=(b_*,t_{2,*}),\qquad
                         c_*=s_{3,*}\in K_3\cup K_4 .           \tag{2}
\]
The last inclusion follows from the full typed images and their
Fourier-reference identification in Section 1 of the
[coherent main-sheet theorem](research_mixed_fourier_prefix_coherent_main_sheet.md).
At \(m=3\), the last vertex is ordinary with its original Fourier
inverse input, and its left leg is in \(O_4\subset K_4\).
Thus every pair of endpoint/ordinary witnesses used in the original
compatibility proof still contains the actual point. This is the
same source transfer already detailed for the stronger 43 bound in
Section 3 of the
[first-attached eligibility theorem](research_mixed_first_attached_taper_root_eligibility.md).
Neither an independent endpoint-disk image nor a two-endpoint
length-two configuration is substituted in (2).

After any additional fixed cutoff in \([0,1]\), it suffices to use
the resulting effective \(c\in[-.078,0]\). Write
\[
 \begin{gathered}
 a=x-i\lambda(x-.1),\quad \lambda=-c/.12,\quad
       0\le\lambda\le13/20,\quad .1\le x\le.22,\\
 r=e^{-2\pi\lambda(x-.1)},\quad e\in[.27,.49],\quad
 s=v+i\eta,\quad v\in[.22,.49],\quad -.108\le\eta\le0 .
 \end{gathered}                                                \tag{3}
\]
The neighboring target \(b\) stays fixed and retains the actual
quadratic upper cutoff and all other hypotheses of the raised-index
barrier. The original joint derivative, with both first-leg
halfweights allocated exactly once, is
\[
 \mathcal H_1(e,v,\eta;x,\lambda)=\Re[(1-i\lambda)D],\qquad
 D=g'(e+a)+g'(s+a)-3g'(a)+2\pi i s .                            \tag{4}
\]
The ordinary chirp is essential. No gauge or original marginal is
removed. The reviewed height and endpoint arguments reduce the
minimum to \(\eta=0\), \(e=.27,.49\), and \(v=.22,.49\).
At \(v=.49\) they already give \(\mathcal H_1>1/300\).

## 2. The right private endpoint decreases to \(x=.22\)

Throughout (3), \(r>3/5\): one has
\(2\pi\lambda(x-.1)\le.156\pi<1/2\), and
\[
 e^{1/2}\le1+\frac12+
 \frac{(1/2)^2}{2(1-(1/2)/3)}=\frac{33}{20}<\frac53.             \tag{5}
\]
Put \(C=(r+r^{-1})/2\le17/15\). At a fixed radius the real cotangent
\[
                 \frac{\sin(2\pi x)}{C-\cos(2\pi x)}            \tag{6}
\]
has no interior minimum on \([.1,.22]\), since its derivative has
the sign of \(C\cos(2\pi x)-1\). The elementary endpoint bounds in
Section 2 of the
[own-three comparison](research_mixed_first_three_moving_height_comparison.md)
give
\[
 \Re\cot\pi a>\frac{147}{143},\quad
 \Re\cot\pi(.22+a)<\frac{50}{71},\quad
                         \Re\cot\pi(.49+a)<0 .                 \tag{7}
\]
For the middle bound use
\(\cos(2\pi(.22+x))<-21/50\) and a sine numerator at most one.

At \(e=.49,v=.22,\eta=0\), write
\[
 \begin{split}
 g''(.49+a)+g''(.22+a)-3g''(a)&=-\pi P+i\pi Q,\\
 P&>\frac{24161}{10153},\\
 Q&=1+\Im\cot\pi(.49+a)+\Im\cot\pi(.22+a)
                                      -3\Im\cot\pi a\le1 .
 \end{split}                                                  \tag{8}
\]
Here \(g''(z)=\pi\cot\pi z-\pi i\).
The last inequality retains the common radius: the three imaginary
cotangents have the same nonnegative numerator, whereas the own
argument has positive angular cosine and both shifted arguments
have negative angular cosine. Each shifted imaginary cotangent
is at most the own one.

Differentiating (4) along the actual path, with \(\lambda\) fixed,
\[
 \frac{d}{dx}\mathcal H_1(.49,.22,0;x,\lambda)
       =-\pi(1-\lambda^2)P+2\pi\lambda Q<0,                     \tag{9}
\]
because
\[
 \frac{231}{400}\frac{24161}{10153}-\frac{13}{10}
                      =\frac{301631}{4061200}>0.              \tag{10}
\]
It suffices to estimate this endpoint at \(x=.22\).

## 3. An exact endpoint logarithm inequality

At \(x=.22\) put
\[
 t=\frac{6\pi}{25}\lambda,\quad q=\tanh(t/2),\quad
 T=\tan(.21\pi),\quad V=\tan(.06\pi),\quad A=\cot(.22\pi).
                                                                    \tag{11}
\]
Then \(0\le q<1/4\) and
\(\lambda=25\operatorname{atanh}q/(3\pi)\).
For \(0<y<1\), the original branch identity is
\[
 g'(y-it/(2\pi))
 =\log(1+e^{-t})+\log\sin\pi y
      +i\pi(1/2-y)+\log(1-iq\cot\pi y).                        \tag{12}
\]
It follows by factoring \(1-e^{-t-2\pi iy}\).
Both sides agree at \(t=0\) with the original strip lift,
and the last factor has positive real part, so no integer
logarithmic lift is introduced.

Define
\[
 P_0=\log\frac{\cos(.21\pi)\cos(.06\pi)}
                         {2\sin^3(.22\pi)}.                   \tag{13}
\]
Substitution of \(y=.71,.44,.22\), including the chirp
\(+.44\pi i\), gives exactly
\[
 \begin{split}
 \Re D={}&P_0+\log(1+q)
       +\tfrac12\log(1+T^2q^2)+\tfrac12\log(1+V^2q^2)
       -\tfrac32\log(1+A^2q^2),\\
 \Im D={}&-\frac{11\pi}{20}
               +\arctan(Tq)-\arctan(Vq)+3\arctan(Aq).
 \end{split}                                                  \tag{14}
\]

Sufficient purely rational trigonometric witnesses are
\[
 \frac{77}{100}<T<\frac45,\quad
 \frac3{16}<V<\frac15,\quad
 \frac65<A<\frac{49}{40},\quad P_0>\frac25 .                   \tag{15}
\]
For completeness put
\[
 \begin{array}{ll}
 S_3(z)=z-z^3/6,&S_5(z)=z-z^3/6+z^5/120,\\
 C_4(z)=1-z^2/2+z^4/24,&
 C_6(z)=1-z^2/2+z^4/24-z^6/720 .
 \end{array}                                                  \tag{16}
\]
On the present interval these are the alternating Taylor
lower/upper bounds. Using \(157/50<\pi<22/7\), the first and
third pairs in (15) follow from the exact rational inequalities
\[
 \begin{array}{rcl}
 S_3(3297/5000)&>&(77/100)C_4(3297/5000),\\
 S_5(33/50)&<&(4/5)C_6(33/50),\\
 C_6(121/175)&>&(6/5)S_5(121/175),\\
 C_4(1727/2500)&<&(49/40)S_3(1727/2500).
 \end{array}                                                  \tag{17}
\]
For \(V\), use \(.06\pi>3/16\), \(\tan z>z\), and
\(.06\pi<19/100\), \(\sin z<19/100\), \(\cos z>49/50\).
The last inequality in (15) follows from
\[
 C_6(33/50)>\frac{7899}{10000},\quad
 1-\tfrac12(33/175)^2>\frac{491}{500},\quad
 S_5(121/175)<\frac{319}{500}.                                 \tag{18}
\]
Their ratio in (13) exceeds
\[
 \frac{96960225}{64923518}>\frac{97}{65}\ \ge\ e^{2/5}.          \tag{19}
\]
The strict cross-product difference is \(4833379\).
The exponential bound is
\(e^z\le1+z+z^2/[2(1-z/3)]\) at \(z=2/5\).
All inequalities (17)--(18) are comparisons of the displayed
rational polynomials; they introduce no numerical sampling.

Set
\[
 k_1=\frac{417}{100},\quad
 k_3=\frac{64}{375}+\frac{117649}{64000}=\frac{77143}{38400},
 \quad c_0=\frac{175}{66}.                                    \tag{20}
\]
Alternating arctangent bounds give
\[
 \arctan(Tq)-\arctan(Vq)+3\arctan(Aq)
                         \ge k_1q-k_3q^3\ge0.                 \tag{21}
\]
Also \(25/(3\pi)>c_0\) and
\(\operatorname{atanh}q\ge q+q^3/3\).
Treat the negative constant in (14) separately:
\[
 -\frac{55}{12}\operatorname{atanh}q
 \ge-\frac{55}{12}\left(q+\frac{q^3}{3}\right)-q^5,             \tag{22}
\]
since the remaining series is at most
\((55/12)q^5/[5(1-q^2)]\le(44/45)q^5\).

The alternating logarithm bounds in (14) now imply
\[
 \mathcal H_1(.49,.22,0;.22,\lambda)
 >\frac25-\frac{43}{12}q+B_2q^2-\frac{43}{36}q^3
                                  +B_4q^4-q^5+B_6q^6,        \tag{23}
\]
with
\[
 \begin{split}
 B_2={}&-\frac12+\frac12(77/100)^2+\frac12(3/16)^2
                     -\frac32(49/40)^2+c_0k_1>\frac{861}{100},\\
 B_4={}&-\frac14-\frac14(4/5)^4-\frac14(1/5)^4
                     +\frac34(49/40)^4+c_0(k_1/3-k_3)>-\frac25,\\
 B_6={}&-\frac12(49/40)^6-c_0k_3/3>-\frac72.
 \end{split}                                                  \tag{24}
\]
For an exact check of the tightest coefficient,
\(B_2-861/100=34879/3520000>0\).
For \(B_4\), use \(3(49/40)^4/4>27/16\) and
\(c_0(k_3-k_1/3)=166369/101376<33/20\).
For \(B_6\), use \((49/40)^6/2<17/10\) and \(c_0k_3/3<9/5\).

Absorbing the higher negative powers with \(q\le1/4\),
\[
 \frac{861}{100}-\frac{43}{144}-\frac1{40}
      -\frac1{64}-\frac7{512}
               =\frac{33}{4}+\frac{817}{115200}>\frac{33}{4}.
                                                                    \tag{25}
\]
Therefore
\[
 \mathcal H_1(.49,.22,0;.22,\lambda)
   >\frac25-\frac{43}{12}q+\frac{33}{4}q^2
   \ge\frac{259}{23760}>\frac1{100}.                           \tag{26}
\]
The quadratic discriminant is \(-259/720<0\).
The case \(\lambda=q=0\) is included by (14)--(15);
no division by a vanishing height occurs.
Together with (9), this proves (26) for every \(x\in[.1,.22]\).

## 4. The left private endpoint

For \(x\ge.12\), the angle of \(.27+x\) is at least as close
to the half-period as that of \(.49+x\).
At the common radius \(r\le1\), its logarithm has at least the
right endpoint's real part. Its original imaginary part is
positive, whereas the right endpoint's is negative.
Since \(\lambda\ge0\),
\[
 \mathcal H_1(.27,.22,0;x,\lambda)
   \ge\mathcal H_1(.49,.22,0;x,\lambda)>\frac1{100},
                          \qquad .12\le x\le.22.              \tag{27}
\]

For \(.1\le x\le.12\), one instead has \(r>9/10\):
\(2\pi\lambda(x-.1)\le.026\pi<1/10\) and \(e^{1/10}<10/9\).
Elementary trigonometric bounds give
\[
 \cos(2\pi(.27+x))<-17/25,\quad
 \cos(2\pi(.22+x))<-21/50,\quad
                         \cos(2\pi x)>18/25.                  \tag{28}
\]
The first two numerator moduli in \(D\) exceed \(17/10\) and
\(8/5\). The own denominator modulus is less than \(3/4\):
its squared upper bound \(1+r^2-(36/25)r\) increases for
\(r\ge9/10\) and equals \(14/25<9/16\) at one. Hence
\[
 \Re D>\log(4352/675)>\log(25/4)>
       4\left(\frac37+\frac{(3/7)^3}{3}\right)=\frac{624}{343}.
                                                                    \tag{29}
\]
Both numerator arguments are nonnegative. The own original argument
is at most \(.4\pi\), and the chirp remains \(+.44\pi\).
Thus \(\Im D\ge-.76\pi\), and
\[
 \mathcal H_1(.27,.22,0;x,\lambda)
          >\frac{624}{343}-\frac{2717}{1750}>\frac14.           \tag{30}
\]
The last difference after subtracting \(1/4\) is
\(2859/171500>0\).

## 5. Complete central/cut transport and remaining terms

**Theorem 1.** On the actual attached reference and target family
of Section 1,
\[
 \mathcal H_1(e,v,\eta;x,\lambda)>\frac1{300}
 \quad(e\in[.27,.49],\ v\in[.22,.49],\ -.108\le\eta\le0).        \tag{31}
\]
The lower ordinary endpoint is paid by (26)--(30), its upper
endpoint has the old bound, and the exact endpoint/height reductions
apply. The moving derivative always retains the actual height
correlation.

The own-four true-end cap exponent is strictly inactive on this
whole early tube, by Proposition 1 of the
[complete cap-envelope transport](research_mixed_cap_early_taper_envelope_transport.md).
It is absorbed with a uniform angular loss before adjoining actions
or Fourier allocations are added. Thus (31) applies to the complete
cap envelope combined with the adjoining central profile or either
real cut \(.22,.49\). Integrating each fixed private profile and
then taking its maximum yields
\[
 \mathcal E(x_0)\le\mathcal E(x_1)-\frac{x_1-x_0}{300},
                         \qquad .1\le x_0<x_1\le.22.           \tag{32}
\]
Only the first target follows \(h=c(x-.1)/.12\);
\(b,\eta\) and the ordinary-color parameter stay fixed.
No smooth dependence of a maximizing index is required.
The central statement covers every adjoining own-four factor
and the nonpositive-index-height subfamily of an adjoining
own-three factor. Both real cuts apply to either adjoining type.
Source qualifications, parities, zeros and fixed color jets
remain those of the complete finite envelope.

Equation (32) still leaves the high physical-tail alternatives
and the two-incidence neighboring-height term in equation (23)
of the moving-height reduction. The reference cap marginal,
synthetic middle compensation and relative pinning fee are unchanged.
No calibrated full-boundary sign, length-two extension, complete
source lower bound or larger knot-family theorem follows here.

