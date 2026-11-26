# A sharper forced maximum and a larger curvature budget

Research deduction, 6 November 2026.

For the first selected type-four coordinate followed by a type-three
vertex, the forced Fourier maximum has real coordinate less than
\(2/5\). The earlier bound was \(41/100\). The improvement comes
from the actual private cap equation, not from an independent choice
of its critical point. It allows a common gap for the two central
Fourier alternatives under the weaker curvature bound
\(G''\le13\pi/2\), in place of \(6\pi\).

The location estimate below is unconditional on the already specified
actual-reference domains. The curvature bound is still an unproved
premise. No estimate for omitted finite rows, connecting currents,
or arbitrary short components is inferred.

## 1. The original variables and the two objectives

Retain the first-cap and next-type-three phase from
[the height-envelope calculation](research_mixed_selected_boundary_height_envelope.md):
\[
\begin{split}
\mathcal F(e,s;z,b)={}&S(e)+g(e+z)+g(s+z)+g(s+b)
       -2g(s)-3g(z)-g(b)-g(e)\\
 &-\frac{i\pi}{2}(e-e^2)+2\pi izs .
\end{split}
\tag{1}
\]
Here \(S\) is the original critical action of the private endpoint,
with its canonical root and logarithmic branch. The factorial
primitive has
\[
 g'(w)=\log(1-e^{-2\pi iw}),\qquad
 g''(w)=\pi\cot(\pi w)-i\pi,
 \qquad J(x)=\Re g(x).
\tag{2}
\]
On the real factorial interval, \(J'(x)=\log(2\sin\pi x)\)
and \(J(1/2)=0\). All logarithms retain their original regular
strip branches. A prescribed real affine function of \(b\) is
subtracted throughout, as in the height-envelope argument; it affects
none of the \(e\)- or \(z\)-derivatives below.

Write \(k=\Im z\), \(x=\Re z\), and keep
\[
 0\le k\le\frac7{500},\qquad \frac{11}{50}\le x\le\frac9{20}.
\tag{3}
\]
The two real objectives, before the common outgoing affine subtraction,
are
\[
 f_{\rm fac}=\Re\mathcal F-2\pi k,
 \qquad f_{\rm force}=\Re\mathcal F+\Re g(z).
\tag{4}
\]
For a word of length at least three, the actual heights obey
\[
 -.051<\Im e<-.019,
 \qquad -.065<\Im s,\Im b<.068.
\tag{5}
\]
At every maximum, the previously proved location estimates give
\[
 .3<\Re e<.4,
 \qquad .2<\Re s\le.5,
 \qquad .22\le\Re b\le.45.
\tag{6}
\]
These are Section 7 and Proposition 7 of the cited note and the
[original optimizer bounds](research_mixed_selected_boundary_optimizer_bounds.md).
The fixed horizontal domain is unchanged. In particular the private
variable can be increased slightly at every point considered below.

## 2. A stronger private-coordinate barrier

**Proposition 1.** Every maximizer of either objective in (4) satisfies
\[
                         \Re e>\frac{153}{500}.
\tag{7}
\]

Put \(D_e=\Re\mathcal F_e\). At \(\Re e=3/10\), its minimum
over the permitted \(x,k\) is at \(x=9/20,k=0\). Indeed
\(\partial_xD_e=\pi\Re\cot\pi(e+z)<0\), since the real sum
ranges from \(.52\) to \(.75\). At \(x=.45\),
\(\partial_kD_e=\pi(1-\Im\cot\pi(e+z))>0\), because that
imaginary cotangent is \(-\tanh(2\pi(\Im e+k))\).

At this reduced pair set
\[
 E=e^{-2\pi ie},\quad r=|E|,\quad
 \gamma=\cos(2\pi/5),\quad\delta=\cos(\pi/5),
 \quad D=\sqrt{E(2-E)}.
\tag{8}
\]
The canonical square root has positive real part. The original
endpoint modulus identity, derived in equation (62) of the
height-envelope note, is
\[
                    e^{D_e}=\frac{\sqrt{1+r^2}}{|1-D|^2}.
\tag{9}
\]
Here
\(7/10<r<9/10\), \(3/10<\gamma<31/100\), and
\(\delta>4/5\). Write \(L=|D|^2\) and \(a=\Re(D^2)\).
Then
\[
 L=r\sqrt{4+4\gamma r+r^2},\qquad
 a=\delta r^2-2\gamma r,\qquad
                    2\Re D=\sqrt{2L+2a}.
\tag{10}
\]
Rationalizing the square root gives the useful improvement
\[
\begin{split}
 \sqrt{4+4\gamma r+r^2}
 &=2+\gamma r+
 \frac{(1-\gamma^2)r^2}
      {\sqrt{4+4\gamma r+r^2}+2+\gamma r},\\
 L&>2r+\frac3{10}r^2+\frac9{50}r^3.
\end{split}
\tag{11}
\]
The denominator in the first line is less than five, whereas
\(1-\gamma^2>9/10\). Inserting (11),
\(a>(4/5)r^2-(31/50)r\), and
\(L^2<4r^2+(31/25)r^3+r^4\) yields
\[
\begin{split}
 2L+2a-(L-1/10)^2&>q(r),\\
 q(r)&=-r^4-\frac{211}{250}r^3-\frac{87}{50}r^2
                    +\frac{79}{25}r-\frac1{100}>0.
\end{split}
\tag{12}
\]
For the last sign, \(q''<0\) on positive radii and
\[
 q(7/10)=\frac{25619}{31250},\qquad
 q(9/10)=\frac{19153}{125000}.
\tag{13}
\]
Since \(L>7/5\), the positive square root in (10) therefore
exceeds \(L-1/10\). Consequently
\[
 |1-D|^2<\frac{11}{10},\qquad
 D_e>\log\frac{\sqrt{149}}{11}>\frac1{10}
                         \quad\text{at }\Re e=3/10.
\tag{14}
\]
The last strict inequality follows, for example, by applying
\(e^t\le1+t+t^2/[2(1-t/3)]\) at \(t=1/10\), squaring,
and comparing with \(149/121\).

It remains to keep this positive derivative while increasing
\(\Re e\) to \(153/500\). Put \(p=\cot\pi e\) and
\(\sigma=-S''(e)/\pi\). The
[canonical endpoint Hessian](research_mixed_pair_curvature_composition.md),
Proposition 2, gives
\[
 \sigma=p+\frac{2(p-i)}{\mathcal R},\qquad
                         \mathcal R^2=E(2-E).
\tag{15}
\]
Its specified square-root sign is retained; only its modulus is
bounded here. On \(.3\le\Re e\le.306\),
\(\cos(2\pi\Re e)<-3/10\). Thus
\[
 |p|^2\le\frac{1+r^2-(3/5)r}{1+r^2+(3/5)r}
       <\frac{107}{191}<\frac9{16},\qquad
 |p-i|^2\le\frac{4r^2}{1+r^2+(3/5)r}
       <\frac{324}{235}<\frac{36}{25}.
\tag{16}
\]
The first rational function decreases for \(r<1\), and the
second increases, so their extrema use \(r=7/10\) and
\(r=9/10\), respectively. Also
\[
 |\mathcal R|^2=r|2-E|\ge r(2+(3/10)r)
        >\frac{1547}{1000}>\frac{36}{25},
 \qquad \Re\sigma<\frac{11}{4}.
\tag{17}
\]
The real sum \(e+z\) lies between \(.52\) and \(.756\).
Its real cotangent is greater than \(-11/10\). One elementary
witness is
\(\cot(.244\pi)=(1+\tan(.006\pi))/(1-\tan(.006\pi))<11/10\),
using \(\tan(.006\pi)<1/21\); an imaginary displacement
only decreases the magnitude of a negative real cotangent.
Equations (15)--(17) give
\[
 -\partial_{\Re e}D_e
 =\pi\Re\{\sigma+p-\cot\pi(e+z)\}<\frac{23\pi}{5}.
\tag{18}
\]
Throughout the interval of length \(3/500\), (14) and (18)
therefore imply
\[
 D_e>\frac1{10}-\frac{69\pi}{2500}
                      >\frac{58}{4375}>0,
\tag{19}
\]
where \(\pi<22/7\). The earlier barrier already excludes
\(\Re e\le.3\). On the remaining interval, increasing the
private coordinate improves both objectives, which proves (7).

## 3. The forced maximum is below two fifths

**Proposition 2.** At every forced maximum under (3)--(6),
\[
                              x<\frac25.
\tag{20}
\]

Suppose instead \(.4\le x\le.45\). Put
\(S_0=e^{-2\pi is}\), \(Z=e^{-2\pi iz}\), and \(R=|Z|\).
The exact marginal, including the original chirp, is
\[
 e^{\partial_x f_{\rm force}}
   =\frac{|1-EZ|\,|S_0^{-1}-Z|}{|1-Z|^2}.
\tag{21}
\]
The new private barrier and (6) give
\[
 \cos(2\pi\Re(e+z))>-\frac{11}{40},\qquad
 \cos(2\pi\Re(s+z))>-\frac{81}{100},\qquad
 \cos(2\pi x)<-\frac{161}{200}.
\tag{22}
\]
For the first inequality use \(\Re(e+z)>.706\) and
\(\sin(.088\pi)<11/40\). The latter follows from the
alternating sine upper polynomial through degree five at
\(242/875>.088\pi\). The other two follow from
\(\cos(\pi/5)=(1+\sqrt5)/4\), using
\(111/50<\sqrt5<56/25\).
The actual height bounds also imply
\[
                  |E|<\frac89,
       \qquad |S_0|^{-1}<\frac{301}{200},\qquad R\ge1.
\tag{23}
\]
For the first, \(.038\pi>2983/25000\), and
\(1+t+t^2/2>9/8\) at that rational value. For the second,
\(.13\pi<143/350\), and the positive-series bound
\[
 e^t\le1+t+\frac{t^2}{2}+\frac{t^3}{6}
                     +\frac{t^4}{24(1-t/5)}
\tag{24}
\]
at \(t=143/350\) is less than \(301/200\). Its difference
from that rational upper target is
\(182827933/551201000000>0\).

Squaring (21) and retaining the negative cosine signs in
(22) gives the direct bound
\[
 e^{2\partial_x f_{\rm force}}
 <\frac{(\frac{64}{81}R^2+\frac{22}{45}R+1)
             (R^2+\frac{24381}{10000}R+\frac{90601}{40000})}
            {(R^2+\frac{161}{100}R+1)^2}<1.
\tag{25}
\]
To verify the last sign, denominator minus numerator equals
\[
 P(R)=\frac{17}{81}R^4+\frac{9053}{11250}R^3
       +\frac{2472487}{4050000}R^2
       -\frac{292901}{900000}R-\frac{50601}{40000}.
\tag{26}
\]
For \(R\ge1\), replace each positive higher power by \(R\).
The resulting lower bound is increasing and its value at one is
\[
                           P(1)=\frac{112129}{3240000}>0.
\tag{27}
\]
Thus the real derivative in (21) is negative. Decreasing \(x\)
slightly is an admissible improvement at every proposed maximum
with \(x\ge.4\), proving (20).

## 4. A common central gap with curvature thirteen pi over two

Let \(c\) be the original negative reference height and \(M\)
the real critical action after the original outgoing tangent has
been subtracted. Let \(G(k)\) be the maximum of that same unselected
real phase over the fixed horizontal domain at height \(k\).
Retain the proved concavity and reference conditions from Section 12
of the height-envelope note:
\[
 c\ge-\frac7{100},\qquad G(c)=M,\qquad G'(c)=0.
\tag{28}
\]

**Conditional consequence.** If the effective curvature satisfies
\(G''\le13\pi/2\) almost everywhere on the optimizing path
from \(c\) to \(H=7/625\), with the regularity supplied by
the height-envelope lemma, then both central objectives have maximum
less than \(M-1/500\) at height \(H\).

Indeed, integrating the curvature with (28) gives
\[
 G(H)-M\le\frac{13\pi}{4}(H-c)^2
               \le\frac{535717\pi}{25000000}.
\tag{29}
\]
For the factorial branch, subtracting \(2\pi H\) yields
\[
 \max f_{\rm fac}-M
       \le-\frac{24283\pi}{25000000}<-\frac1{500}.
\tag{30}
\]
For the forced branch, Proposition 2 applies since
\(H<7/500\). On its maximizing set,
\(\Re g(x+iH)\le\Re g(2/5+iH)\). The real derivative
\(\log|1-e^{-2\pi i(x+iH)}|\) is positive on the original
plateau, which justifies this monotonicity. The original argument
bound gives
\[
 \Re g(2/5+iH)\le J(2/5)-\frac{\pi H}{10},
                 \qquad J(2/5)<-\frac{133}{2000}.
\tag{31}
\]
For the second inequality, \(J'\) is concave on \([2/5,1/2]\),
with endpoint values greater than \(16/25\) and \(69/100\).
Its integral is therefore greater than the trapezoid of these
two lower bounds. To verify the first endpoint explicitly,
\(2\cos(\pi/10)>2329/1225\), whereas (24) at \(16/25\)
is less than this number. The second endpoint follows from
\(\log2>2(1/3+1/81+1/1215)>69/100\).

Combining (29)--(31), with \(\pi<22/7\), proves
\[
 \max f_{\rm force}-M
 <\frac{507717\pi}{25000000}-\frac{133}{2000}
 <-\frac{233863}{87500000}<-\frac1{500}.
\tag{32}
\]

The new comparison spends the factorial credit only after restricting
the actual forced maximizing point. The allowed curvature has
increased from \(6\pi\) to \(13\pi/2\), while the same strict
central gap is retained. Proving that curvature bound on the actual
maximizing path, and estimating the remaining finite-source sectors,
are still necessary. This note changes neither the original heights
nor the selected geometric reference and introduces no new knot
volume conclusion.
