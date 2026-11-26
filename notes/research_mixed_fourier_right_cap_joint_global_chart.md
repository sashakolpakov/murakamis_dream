# A joint global chart for the central retained rows

Research deduction, 7 November 2026. The numerator factorial is
holomorphic across the triangular support wall. Its zeros enforce
the physical termination there. Together with the reciprocal
factorial and the global cardinal interpolation, this gives one
exact two-index chart on the central retained interval and the
entire outgoing period.

This statement concerns the original source and its available
contours. It asserts no derivative sign, alias estimate, calibrated
rate or whole-source asymptotic.

## 1. The numerator factorial beyond its first positive wall

Fix \(N\ge2\). The specified Gamma product is
\[
 G_N(w)=\left(\frac{2\pi}{N}\right)^w\Gamma(w+1)
 \prod_{k=1}^{\infty}
 \frac{\Gamma(Nk+w+1)}
      {\Gamma(Nk-w)(Nk)^{2w+1}} .
 \tag{1}
\]
Its original normalization and recurrence are proved in
[the factorial construction](exact_factorial_interpolation_and_complex_contours.md).
As there, positive-base powers use their real logarithms. Put
\[
 \Pi_N(z)=G_N(Nz)
       \exp\!\left\{\frac{\pi i}{2}[N(z-z^2)-z]\right\}.
 \tag{2}
\]

**Lemma 1.** Formula (1) extends \(G_N\) holomorphically to
\(\Re w>-1\). Consequently \(\Pi_N\) is holomorphic on
\(\Re z>-1/N\). Its only zeros there are
\[
 z=J/N,\qquad J=N,N+1,\ldots,
 \quad\text{of multiplicity }\lfloor J/N\rfloor .
 \tag{3}
\]
The exact recurrence and physical values remain
\[
 \Pi_N(z+1/N)=(1-e^{-2\pi i(z+1/N)})\Pi_N(z),\qquad
 \Pi_N(j/N)=P_j\quad(0\le j<N).
 \tag{4}
\]

*Proof.* On \(\Re w>-1\), \(\Gamma(w+1)\) and every numerator
\(\Gamma(Nk+w+1)\) are holomorphic and nonzero. The reciprocal
Gamma factor \(1/\Gamma(Nk-w)\) is entire. On any compact subset,
all sufficiently large factors have logarithms given by the
same locally uniform expansion used in the original proof,
\[
 \log\frac{\Gamma(Nk+w+1)}
              {\Gamma(Nk-w)(Nk)^{2w+1}}
 =-\frac{w(w+1)(2w+1)}{6N^2k^2}+O_K(k^{-3}).
 \tag{5}
\]
Thus their product converges normally to a nonzero holomorphic
function. The finitely many remaining factors are holomorphic
and retain their zeros.

A zero occurs precisely when \(Nk-w\) is a nonpositive integer,
so \(w=J\ge N\) is an integer. For this \(J\), there is one
simple zero from each \(1\le k\le\lfloor J/N\rfloor\).
No numerator pole or zero cancels it. This proves (3).
The recurrence, initially proved on the original overlap,
extends as a holomorphic identity on the enlarged half-plane.
The physical values in (4) are unchanged. \(\square\)

Let \(E_N\) be the reciprocal continuation from
[the global cardinal chart](research_mixed_fourier_global_factorial_cardinal.md).
It is holomorphic on \(\Re z<1\), with zeros at
\(-J/N\), \(J\ge1\), of multiplicity \(\lceil J/N\rceil\).
On the common strip \(-1/N<\Re z<1\),
\[
                         \Pi_N(z)E_N(z)=1.
 \tag{6}
\]
This follows by continuation from \(0<\Re z<1\), and includes
\(z=0\). The two extensions serve different purposes:
positive support walls belong to the numerator \(\Pi_N\);
negative reciprocal walls belong to \(E_N\).

## 2. An exact central-index, full-period source

Keep the original parameters
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(Z)=(rZ;r)_j,\quad X=e^{-2\pi ia},\quad Y=e^{2\pi iy},
 \qquad \Re a\in[11/50,9/20],\quad y=x_0.
 \tag{7}
\]
The heights of \(a\) are its actual correlated heights. No
height enlargement of a source estimate is assumed here.
Use the original global cardinal function
\[
 \widehat f_N(q;y)=
 \frac{e^{-\pi i(N-1)y}}{N}e^{2\pi iNyq}
       \Pi_N(1-y-1/N)E_N(q-y).
 \tag{8}
\]
Its domain is \(\Re q<1+\Re y\), with arbitrary finite imaginary
height, and \(\widehat f_N(l/N;y)=f_l(y)\) for every \(0\le l<N\).
All its zeros and its exact scalar are part of (8).

Set
\[
 L_N=\lceil N/8\rceil,\qquad M_N=\lceil N/2\rceil-1.
 \tag{9}
\]
For \(N\ge3\), \(1\le L_N\le M_N<N\). At \(N=2\) the
central retained range is empty and its source is zero.
The remaining low rows \(0\le j<L_N\) continue to carry
their complete outgoing sums; nothing below estimates them.

Define
\[
 \boxed{\quad
 T_N(s,q;a,y)=e^{2\pi iNas}
  \Pi_N(s+a)\Pi_N(s+q)
  E_N(a)E_N(q)E_N(s)^3\,\widehat f_N(q;y).
 \quad}
 \tag{10}
\]
For physical \(L_N\le j\le M_N\) and \(0\le l<N\),
the exact recurrence gives
\[
 T_N(j/N,l/N;a,y)=
 \begin{cases}
 \displaystyle
 \frac{X^{-j}p_j(X)P_{j+l}}{P_j^3P_l}\,f_l(y),
                                  &j+l<N,\\[2mm]
 0,                               &j+l\ge N .
 \end{cases}
 \tag{11}
\]
Indeed \(\Pi_N(a+j/N)E_N(a)=p_j(X)\),
\(E_N(j/N)=P_j^{-1}\), and \(E_N(l/N)=P_l^{-1}\).
The second line follows from the actual numerator zero (3);
all other factors are regular. It is not obtained by extending
an inverse factorial through that wall.

More generally, for each fixed physical \(j\) in (9), throughout
\(-1/N<\Re q<1\) and the domain of (8), (4) and (6) give
\[
 T_N(j/N,q;a,y)=
       \frac{X^{-j}p_j(X)}{P_j^3}
           p_j(e^{-2\pi iq})\widehat f_N(q;y).
 \tag{11a}
\]
This is an off-grid identity in \(q\), including the added
wrap region, not just an equality of physical lattice values.

Consequently the exact central retained source is
\[
 \begin{split}
 V_N^{\mathrm{cen}}
 &=\sum_{j=L_N}^{M_N}\sum_{l=0}^{N-1}
                             T_N(j/N,l/N;a,y)\\
 &=\sum_{j=L_N}^{M_N}
       \frac{X^{-j}p_j(X)}{P_j^3}
                \sum_{l=0}^{N-j-1}p_j(r^l)f_l(y).
 \end{split}
 \tag{12}
\]
This is the corresponding subset of the original low-index
source, with each whole outgoing \(H_{j,N}\) retained.
There is no new crossing scalar or power of \(N\).
The cardinal \(1/N\) in (8), incoming Fourier factor, and
any exterior incoming halfweight remain exactly allocated.

## 3. Holomorphy on joint rectangles

Use the half-grid real endpoints
\[
 \sigma_-=\frac{L_N-1/2}{N},\qquad
 \sigma_+=\frac{M_N+1/2}{N},\qquad
 \alpha_N=-\frac1{2N},\qquad
 \beta_N=1-\frac1{2N}.
 \tag{13}
\]
The upper retained endpoint is
\[
 \sigma_+=
 \begin{cases}
 1/2-1/(2N),&N\text{ even},\\
 1/2,&N\text{ odd}.
 \end{cases}
 \tag{14}
\]
Choose arbitrary finite lower and upper heights for each
variable, with the real axis strictly between them.

**Proposition 2.** For \(N\ge3\), \(T_N\) is holomorphic on
a neighborhood of the product of these two closed rectangles.

*Proof.* The reciprocal factors have
\[
 0<\Re s\le1/2<1,\qquad
 -1/(2N)\le\Re q\le1-1/(2N)<1,\qquad
 0<\Re a<1.
 \tag{15}
\]
For the two numerator factorials,
\[
 \Re(s+a)>0,\qquad
 \Re(s+q)\ge\frac{L_N-1}{N}\ge0>-1/N.
 \tag{16}
\]
Thus every factor is in its proved holomorphic domain.
Finally \(\Re q\le\beta_N<1<1+\Re y\), so (8) is
regular throughout. All inequalities needed for the domains
are strict at the corresponding domain boundary, hence persist
on a neighborhood of the compact rectangles. The argument
places no restriction on their finite heights. \(\square\)

In particular the joint contour can cross \(s+q=1\).
At real physical nodes beyond that wall, the source has the
zeros required by (11). At general off-grid points its
numerator is retained, not set to zero. All zeros on the
chosen product domain remain holomorphic zeros; they are
not poles to be avoided.

Let \(\Gamma_s,\Gamma_q\) be the positively oriented boundaries
of the two rectangles. The exact finite residue formula is
\[
 V_N^{\mathrm{cen}}=
 \frac1{(2\pi i)^2}
 \int_{\Gamma_s}\int_{\Gamma_q}
 T_N(s,q;a,y)
       \{\pi N\cot(\pi Ns)\}\{\pi N\cot(\pi Nq)\}\,dq\,ds .
 \tag{17}
\]
Each cotangent factor has residue one at its indicated physical
node. Proposition 2 leaves no additional interpolation poles
inside, and (11) supplies the literal supported source.
Equation (17) holds for both parities with the cuts (13)--(14).

## 4. The available deformation and the remaining estimates

Equation (17) permits a joint analysis of the central retained
rows with the whole outgoing period, without introducing cuts
at outgoing real parts \(.22\) and \(.45\). It is compatible
with the exact one-index
[main-plus-boundary formula](research_mixed_fourier_factorial_alias_elimination.md):
on a physical retained node, (10) is its same global
cardinal source, including the off-grid polynomial extension.
Keeping its complete contour before taking a modulus
preserves cancellation across any later artificial cuts.

The uniform compact-strip factorial symbol is not automatically
valid across a numerator zero, or across a reciprocal zero.
Lemma 1 and Proposition 2 prove exact holomorphy and source
identification there, not a nonvanishing leading approximation.
Nor does this construction estimate the central main path
outside its previously controlled domain, the signed vertical
boundary current, or the remaining rows \(j<L_N\).
Derivative signs, calibrated complement bounds and a
whole-source lower asymptotic require their own proofs.
No numerical evaluation or certificate replay is used.
