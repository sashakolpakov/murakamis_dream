# Finite lattice contours for the adjacent two-crossing sum

Research note, 2 November 2026. This note separates two questions in
the remaining adjacent-pair calculation. First, a polygonal set of
integer indices has an exact contour formula with every endpoint
current and every Fourier correction retained. A rectangular
replacement of the triangular support is unnecessary. Second, the
most direct proposed contour does **not** give an absolute exponential
bound for one of those corrections. The latter statement has an
elementary proof; it is not based on a numerical maximization.

Neither statement proves an asymptotic for the whole adjacent-pair
source. The proved extreme-index bounds remain valid, and the selected
upper contour remains a possible part of a successful deformation.
The other contour terms still have to be treated.

## 1. A finite set of cells and its exact contour

Let \(\mathcal I_N\subset\mathbb Z^2\) be any finite set of retained
indices. For the adjacent pair it is the set left after the four
extreme-index restrictions in
[the tail theorem](research_adjacent_two_crossing_global_tails.md).
Put
\[
 I_i=\left[\frac{i-1/2}{N},\frac{i+1/2}{N}\right],
 \qquad
 P_N=\bigcup_{(i,j)\in\mathcal I_N} I_i\times I_j .
 \tag{1}
\]
These are actual half-grid cells. In particular, there is no
approximation in replacing the index set by \(P_N\).

Fix positive heights \(h_1,h_2\). Suppose \(f_N(z_1,z_2)\) is
holomorphic on a neighborhood of every product
\[
 (I_i+i[-h_1,h_1])\times(I_j+i[-h_2,h_2])
 \quad ((i,j)\in\mathcal I_N).
 \tag{2}
\]
For one variable and a half-grid interval \(I=[a,b]\), define
\[
\begin{aligned}
 U_I f&=N\int_a^b f(x+ih)\,dx,\\
 U_I^{\rm corr}f
 &=N\int_a^b f(x+ih)
     \frac{e^{2\pi iN(x+ih)}}{1-e^{2\pi iN(x+ih)}}\,dx,\\
 L_I^{\rm corr}f
 &=N\int_a^b f(x-ih)
     \frac{e^{-2\pi iN(x-ih)}}{1-e^{-2\pi iN(x-ih)}}\,dx,\\
 E_I f
 &=-iN\int_{-h}^{h}
       \frac{f(b+is)-f(a+is)}{1+e^{-2\pi Ns}}\,ds .
\end{aligned}
\tag{3}
\]
The height is \(h_1\) or \(h_2\) according to the variable.
The [one-sided residue identity](research_terminal_one_sided_wire_formula.md)
gives
\[
 f(i/N)=(U_{I_i}+U_{I_i}^{\rm corr}
                     +L_{I_i}^{\rm corr}+E_{I_i})f.
 \tag{4}
\]
It follows, by applying (4) in the two coordinates, that
\[
 \boxed{\displaystyle
 \sum_{(i,j)\in\mathcal I_N} f_N(i/N,j/N)
  =\sum_{(i,j)\in\mathcal I_N}
    (U_i+U_i^{\rm corr}+L_i^{\rm corr}+E_i)
    (U_j+U_j^{\rm corr}+L_j^{\rm corr}+E_j)f_N.}
 \tag{5}
\]
All sums and contour integrals in (5) are finite, apart from optional
geometric-series expansions of the displayed rational kernels.
Thus no exchange of an infinite Fourier series with its boundary
values is needed.

There is useful cancellation before estimating (5). The term \(U_iU_j\)
sums to
\[
 N^2\int_{P_N} f_N(x+ih_1,y+ih_2)\,dx\,dy.
 \tag{6}
\]
Every other product of two horizontal terms is also an integral over
the same \(P_N\), at its stated pair of heights and with its stated
weights. Terms \(E_iU_j\), \(E_iU_j^{\rm corr}\), and
\(E_iL_j^{\rm corr}\) cancel on a vertical side shared by two cells.
The analogous cancellation holds on horizontal shared sides.
Only sides of the boundary of \(P_N\) remain.

In the terms \(E_iE_j\), the coefficient of a vertical two-parameter
current at a corner is the alternating sum of the indicators of
the four adjacent cells. It is zero at an interior corner and along
a straight boundary segment. Nonzero corner currents remain at
turns of the polygonal boundary, including the corners of its
staircase approximation to an oblique side. They must not be
discarded. Equation (5) proves these cancellations directly, with
their orientations, without a multivariable residue theorem.

For a fixed polygon cut out by finitely many linear inequalities,
there are polynomially many boundary sides and corners. Even the
weaker bound \(O(N^2)\) is enough for exponential estimates.

## 2. A sufficient transfer lemma

The following criterion records precisely what an absolute contour
argument would have to prove.

Assume that \(P\) is a fixed compact polygon and that
\(P_N\mathbin{\triangle}P\) is contained in a \(C/N\) neighborhood
of \(\partial P\), for a constant \(C\) independent of \(N\).
This is satisfied by retaining all grid points obeying the fixed
linear inequalities; Hausdorff proximity alone would not exclude
holes near a saddle. Assume also that \(f_N\) has the uniform expansion
\[
 f_N(z_1,z_2)
   =N^\kappa a(z_1,z_2)e^{NW(z_1,z_2)}
                       (1+O(N^{-1}))
 \tag{7}
\]
on a fixed neighborhood of all the contours in (5).
The functions \(a,W\) are holomorphic and independent of \(N\).
A uniform polynomial bound times \(e^{N\Re W}\) on the other
contours would suffice there in place of the relative expansion.

Assign the following heights and exponential penalties to each
horizontal term:
\[
\begin{array}{c|c|c}
\text{term}&\text{height}&\text{penalty}\\ \hline
U&h&0\\
U^{\rm corr}&h&2\pi h\\
L^{\rm corr}&-h&2\pi h.
\end{array}
\tag{8}
\]
An endpoint current at height \(s\in[-h,h]\) has penalty
\[
                         2\pi(-s)_+.
 \tag{9}
\]
Indeed its weight in (3) is at most \(1\) for \(s\ge0\), and at
most \(e^{-2\pi N|s|}\) for \(s\le0\). The horizontal correction
weights are at most
\[
 \frac{e^{-2\pi Nh}}{1-e^{-2\pi Nh}}.
 \tag{10}
\]
These are bounds for their full rational kernels, hence for all
Fourier modes together.

Suppose the upper contour in (6) contains one critical point
\(z_*=(x_*+ih_1,y_*+ih_2)\), with real projection in the interior
of \(P\). Assume \(a(z_*)\ne0\), the real part of \(-W''(z_*)\)
is positive definite, and
\[
 \Re W(x+ih_1,y+ih_2)<M:=\Re W(z_*)
 \tag{11}
\]
away from that point, with a fixed gap outside every fixed
neighborhood.

For some fixed \(\delta>0\), require each of the following on the
actual indicated contours:

1. For each of the eight other products of horizontal terms, the
   real phase minus its two penalties in (8) is at most \(M-\delta\).
2. On each boundary side current, the real phase minus its endpoint
   penalty (9) and its other horizontal penalty is at most
   \(M-\delta\).
3. On every nonzero corner current, the real phase minus the sum of
   its two penalties (9) is at most \(M-\delta\).

It is enough that these inequalities hold on fixed neighborhoods of
the limiting sides and corners, so that their \(O(N^{-1})\)
half-grid displacement is allowed. For the two-parameter corner
bound this includes every limiting side along which staircase
corners accumulate, not only the finitely many vertices of \(P\).

**Lemma.** Under these hypotheses,
\[
 \sum_{(i,j)\in\mathcal I_N} f_N(i/N,j/N)
  =N^{\kappa+1}
    \frac{2\pi a(z_*)}{\sqrt{\det[-W''(z_*)]}}\,
    e^{NW(z_*)}(1+O(N^{-1})).
 \tag{12}
\]
The square root is the Gaussian branch determined by the oriented
upper contour. The conclusion is uniform in sufficiently small
holomorphic external parameters if the hypotheses have uniform slack.

**Proof.** Equations (5), (8)--(10) bound every nonprincipal term
by a fixed power of \(N\) times \(e^{N(M-\delta)}\). The number of
terms and the lengths and areas of their parameter domains introduce
only polynomial factors. This includes the lower part of every
endpoint current and every staircase corner.

Only (6) remains. Its saddle has positive distance from the
boundary. A fixed neighborhood of it is therefore contained in
\(P_N\) for all sufficiently large \(N\), and (11) bounds the
remainder exponentially. Holomorphic stationary phase in the two
real integration variables gives a factor \(2\pi/N\).
Multiplying this by \(N^2N^\kappa\) gives (12). The nonvanishing
coefficient follows from the accretive Hessian and \(a(z_*)\ne0\).
Small external parameters move the saddle holomorphically; a local
deformation reaches it while the strict exterior inequalities
persist. This proves the uniform statement. \(\square\)

For the adjacent-pair interpolant, \(\kappa=-1\); thus (12) would
give power \(N^0\). The lemma is only a sufficient criterion.
In particular, a valid estimate on the upper surface is not a
substitute for conditions 1--3.

## 3. One actual horizontal correction exceeds the selected rate

Use the exact phase of the adjacent pair at complete boundary:
\[
 W(x,y)=J(x+y)-3J(x)-6J(y)+J(2y)
              +i\pi(x^2-xy+y^2/2+x+y/2).
 \tag{13}
\]
Its selected point has heights
\[
 h_1=\frac{3\log2}{4\pi},\qquad
 h_2=\frac{\log7}{4\pi}.
 \tag{14}
\]
The product \(L_1^{\rm corr}U_2\) in (5) has effective real phase
\[
 B(x,y)=\Re W(x-ih_1,y+ih_2)-2\pi h_1.
 \tag{15}
\]
The rational point \((x,y)=(1/3,1/6)\) is strictly inside the
retained polygon in the tail theorem. We prove
\[
 \boxed{\displaystyle
 B(1/3,1/6)>\frac{4609}{4400}>1,
 \qquad M<\frac{12297}{12560}<1.}
 \tag{16}
\]
Thus condition 1 of the transfer lemma fails for the proposed
constant heights. This failure concerns an absolute estimate for a
contour term. It does not determine the value of that oscillatory
integral.

### 3.1. The upper bound on the selected action

Let
\[
 X=\frac{5+i\sqrt7}{16},\qquad Y=\frac{i}{\sqrt7},\qquad
 a=\frac{\arg X}{2\pi}.
\]
The canonical logarithmic branches give the exact expression
\[
\begin{aligned}
 M={}&\frac{3\log2+\log7}{8}
      +a\left(-3\log2+\frac{\log7}{2}\right)\\
 &+\frac{3\Im\operatorname{Li}_2(X)
          +6\Im\operatorname{Li}_2(Y)
          -\Im\operatorname{Li}_2(XY)}{2\pi}.
\end{aligned}
\tag{17}
\]
This is the same identity used in the proved tail theorem.
The coefficient of \(a\) is negative, since \(7<64\).
The elementary inequalities \(\log2<7/10\), \(\log7<2\)
therefore bound the first line by \(41/80\).

The convergent dilogarithm series gives
\[
 \Im\operatorname{Li}_2(X)
 \le\Im X+\frac{|X|^2}{4(1-|X|)}
 <\frac16+\frac1{20}=\frac{13}{60},
 \tag{18}
\]
because \(|X|^2=1/8\) and \(|X|<3/8\).
For purely imaginary \(Y\), the alternating series gives
\[
 \Im\operatorname{Li}_2(Y)<\frac1{\sqrt7}<\frac{19}{50}.
 \tag{19}
\]
Also \(\Im\operatorname{Li}_2(XY)>0\). One direct proof is to
use the integral of \(-\log(1-tXY)/t\) for \(0<t<1\):
\(XY\) is in the upper half-plane, so the integrand has positive
imaginary part.
Using \(\pi>157/50\), the second line of (17) is consequently
less than
\[
 \frac{13/20+57/25}{2\pi}
 <\frac{293}{628}.
 \tag{20}
\]
Adding \(41/80\) gives the upper bound in (16).

### 3.2. The lower bound on the correction

For \(0<r<1\) and \(h\ge0\), the same canonical branch gives
\[
 \Re J(r+ih)
 =-\frac{\Im\operatorname{Li}_2(e^{-2\pi h+2\pi ir})}{2\pi}
                     -\frac{\pi h}{2}(1-2r).
 \tag{21}
\]
It is unchanged on replacing \(h\) by \(-h\).
In particular \(\Re J(1/2+it)=0\) for every real \(t\).
Substitute \((1/3-ih_1,1/6+ih_2)\) in (13). The polynomial
terms simplify exactly, giving
\[
 B(1/3,1/6)
   =\frac{\log7}{3}
     +\frac{3\Im\operatorname{Li}_2(A)
             +6\Im\operatorname{Li}_2(B_0)
             -\Im\operatorname{Li}_2(C)}{2\pi},
 \tag{22}
\]
where
\[
 A=\frac{e^{2\pi i/3}}{\sqrt8},\qquad
 B_0=\frac{e^{\pi i/3}}{\sqrt7},\qquad
 C=\frac{e^{2\pi i/3}}7.
 \tag{23}
\]
For the first dilogarithm,
\[
 \Im\operatorname{Li}_2(A)
 >\frac{\sqrt6}{8}-\frac1{20}>\frac14.
 \tag{24}
\]
For the second, retain its first two terms:
\[
\begin{aligned}
 \Im\operatorname{Li}_2(B_0)
 &>\frac{\sqrt{21}}{14}+\frac{\sqrt3}{56}
        -\frac{|B_0|^3}{9(1-|B_0|)}\\
 &>\frac8{25}+\frac3{100}-\frac1{75}
   =\frac{101}{300}.
\end{aligned}
\tag{25}
\]
Here \(|B_0|<2/5\) makes the omitted tail less than
\(8/675<1/75\); all the radical comparisons follow by squaring
positive rational numbers. Finally,
\[
 |\operatorname{Li}_2(C)|<\frac{|C|}{1-|C|}=\frac16.
 \tag{26}
\]
The inequalities \(\log7>19/10\) and \(\pi<22/7\) give
\[
 B(1/3,1/6)>
  \frac{19}{30}
    +\frac7{44}\left(\frac34+\frac{101}{50}-\frac16\right)
  =\frac{4609}{4400}.
 \tag{27}
\]
This proves (16) using the actual branches and the complete
correction penalty.

## 4. What happens as the lower height tends to infinity

There is a simple limiting action behind this difficulty.
For \(0<\Re z<1\) and \(\Im z\to-\infty\), the canonical branch
has
\[
 J(z)=-\frac{i\pi}{2}z(1-z)+\frac{i\pi}{12}
                               +O(e^{2\pi\Im z}).
 \tag{28}
\]
For \(y\) in a fixed compact set and with all real parts still
in their original strips, substitution in (13) gives
\[
 W(x,y)-2\pi ix
   =V(y)+O(e^{2\pi\Im x}),\qquad
 V(y)=-6J(y)+J(2y)+i\pi y^2-\frac{i\pi}{6}.
 \tag{29}
\]
The limiting phase is independent of \(x\). Thus sending the
lower side farther down does not create an arbitrarily large
exponential loss.

The equation \(e^{V'(y)}=1\), with \(Z=e^{2\pi iy}\), is
\[
 \frac{Z^2(1+Z)^2}{(1-Z)^4}=1.
 \tag{30}
\]
One root is \(Z=1/3\), on the real-part-zero boundary. The
nonreal roots satisfy \(2Z^2-Z+1=0\). The upper root
\[
 Z=\frac{1+i\sqrt7}{4},\qquad
 y=\frac{\log Z}{2\pi i},
 \quad \Im y=\frac{\log2}{4\pi},
 \tag{31}
\]
also solves the unexponentiated equation \(V'(y)=0\).
Indeed \(1/6<\Re y<1/4\), and the arguments of both
\(\sin\pi y\) and \(\sin2\pi y\) lie between zero and \(\pi/4\).
For the first this follows from
\(\cot(\pi\Re y)<\sqrt3<2\) and
\(\tanh(\pi\Im y)<\log2/4<1/2\); the second is even
smaller. Hence the imaginary part of
\[
 V'(y)=-6\log(2\sin\pi y)
       +2\log(2\sin2\pi y)+2\pi iy
\]
lies strictly between \(-3\pi/2\) and \(\pi\). The only possible
multiple of \(2\pi i\) is zero.

The leading interpolant density from the adjacent-pair calculation
also has a limit:
\[
 a(x,y)=\frac{i\,e^{-2\pi ix}}{4\sin^2\pi y}
                       (1+O(e^{2\pi\Im x})).
 \tag{32}
\]
In particular it decays as \(e^{2\pi\Im x}\). This decay is
separate from the limiting exponential action. To use it in an
asymptotic theorem one would need estimates uniform in a moving
height, together with the complete endpoint currents. Neither is
asserted here.

## 5. Consequence for the remaining proof

The cell formula (5) provides an exact way to keep the original
triangular support. It requires no extension across the factorial
boundary \(x+y=1\), and its half-grid staircase is harmless provided
the stated boundary-current bounds are actually proved.

The fixed-height absolute criterion is presently unavailable:
equation (16) explicitly contradicts one of its required
inequalities. A successful proof must therefore estimate cancellation
inside the lower-\(x\) correction, find a different coupled contour,
or combine contour currents before taking absolute values. The
existence and dominance of the selected upper stationary point do
not settle this issue.
