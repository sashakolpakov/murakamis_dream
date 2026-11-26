# A full-period contour for the adjacent two-crossing source

Research assembly lemma, 2 November 2026. The factorial numerator
vanishes at every additional integer point obtained by extending the
triangular sum to a rectangle. On that rectangle the two vertical
sides of the first contour can be combined by an exact translation
law. This removes the staircase currents that obstruct separate
absolute estimates on the triangular cells.

The statement below is an exact finite identity, followed by a list of
the estimates it needs. It includes both level parities and the actual
half-grid shifts. The lower first-variable contours are already
controlled by the complete-circle theorem. Bounds for the remaining
grouped surfaces are separate inputs to a full asymptotic theorem.

## 1. The rectangular extension is exact

Fix \(\epsilon=10^{-6}\), \(D=N-1\), and put
\[
 L_N=\lceil \epsilon N\rceil,\qquad
 R_N=\lfloor (1/2-\epsilon)N\rfloor .
 \tag{1}
\]
In this note \(R_N\) with an integer subscript in (1) denotes
an upper index; the translation multiplier below is denoted
\(\mathcal R_N\).
Discarding the terms outside this \(j\)-range has a proved
exponential gap by
[the extreme-index theorem](research_adjacent_two_crossing_global_tails.md).
Keep all the original \(i\)-indices.

The exact retained source is
\[
 Z_N^{\rm ret}(u)
   =\sum_{j=L_N}^{R_N}\sum_{i=0}^{N-1} f_N(i/N,j/N;u),
 \tag{2}
\]
where \(f_N\) is the exact interpolant
\[
\begin{aligned}
 f_N(x,y;u)={}&N^2
 e^{i\pi N(x^2-xy+y^2/2+x+y/2)-i\pi(x+y/2)}\\
 &\qquad\cdot
 \frac{G_N(N(x+y))}{G_N(Nx)^3G_N(Ny)^2}\,
                     \mathcal B_N(y,u).
\end{aligned}
\tag{3}
\]
This is the same summand as in the original triangular formula.
Indeed \(G_N(i+j)=0\) whenever \(N\le i+j\le2N-2\).
The exact shift
\[
                 G_N(z+N)=-2\sin(\pi z)G_N(z)
 \tag{4}
\]
proves the assertion from \(G_N(k)\ne0\) for \(0\le k<N\).
All denominator indices \(i,j\) remain below \(N\).
Thus every newly added lattice value in (2) is exactly zero.
No new quantum source is defined.

Put
\[
 a_N=-\frac1{2N},\quad b_N=1-\frac1{2N},\quad
 c_N=\frac{L_N-1/2}{N},\quad d_N=\frac{R_N+1/2}{N}.
 \tag{5}
\]
The \(x\)-interval has length exactly one and encloses precisely
the \(N\) original grid points. The \(y\)-interval encloses
precisely the surviving low indices. These are half-grid
endpoints at both parities.

For all sufficiently large \(N\), (3) is holomorphic on the
closed contour domains used below. Its \(x\)-denominator
has \(-1<\Re(Nx)<N\), where \(G_N\) is nonzero. The
numerator has real part between zero and \(2N\); (4)
continues it holomorphically there, with zeros but no
poles. The \(y\)-factorials stay in their regular strips
for \(u\) in a sufficiently small fixed disk.
For estimates throughout the real boundary period, the
reciprocal-factorial form of \(\mathcal B_N\) retains
its moving zeros as in
[the uniform boundary lemma](research_uniform_factorial_and_boundary_decay.md).

## 2. Heights chosen before applying the residue identities

Set
\[
 h_x=\frac{3\log2}{4\pi},\qquad
 h_y=\frac{\log7}{4\pi},\qquad
 h_a=\frac{\log2}{4\pi},\qquad
 \delta=10^{-5}.
 \tag{6}
\]
The \(x\)-rectangle has heights \(h_x\) and \(-1\).
At each point of its contour let the upper \(y\)-height be
\[
 v(s)=
 \begin{cases}
 \delta+(h_a-\delta)(-s),&-1\le s\le0,\\
 \delta+(h_y-\delta)s/h_x,&0\le s\le h_x,
 \end{cases}
 \qquad s=\Im x .
 \tag{7}
\]
The lower \(y\)-height is always \(-h_y\).
Thus \(v(-1)=h_a\), \(v(h_x)=h_y\), and
\(v(s)\ge\delta>0\).

Use the asymmetric one-variable identity
\[
 \sum_{a<k/N<b}F(k/N)
   =U^{p}F+C_+^{p}F+C_-^{m}F+E^{p,m}F
 \tag{8}
\]
from
[the adaptive residue lemma](research_adjacent_pair_adaptive_lattice_contour.md).
Here \(U^p\) is the constant upper integral with coefficient
\(N\); \(C_+^p,C_-^m\) retain the complete rational
horizontal correction kernels; and
\[
 E^{p,m}F=-iN\int_{-m}^{p}
          \frac{F(b+is)-F(a+is)}{1+e^{-2\pi Ns}}\,ds .
 \tag{9}
\]
Apply (8) in \(x\) first, and then in \(y\) at each fixed
complex \(x\), using (7). This is an exact substitution.
The piecewise linear dependence of the height on \(s\)
introduces no additional connector or Jacobian.

## 3. Combine the two \(x\)-sides before estimating

The exact translation multiplier of (3) is
\[
 \mathcal R_N(x,y)
   =\frac{1-(w/Y)^N}{(1-w^N)^3},\qquad
       w=e^{-2\pi ix},\quad Y=e^{2\pi iy},
 \qquad
 f_N(x+1,y;u)=\mathcal R_N(x,y)f_N(x,y;u).
 \tag{10}
\]
It follows from (4), including the exponential factor in (3).
The signs and normalization are also checked in
[the exact gauge note](research_adjacent_pair_cyclotomic_gauge.md).

On the left side \(x=a_N+is\), write
\[
                         T=e^{2\pi Ns}>0.
 \]
Because \(Na_N=-1/2\), one has \(w^N=-T\) exactly. Hence
\[
 \mathcal R_N(a_N+is,y)
              =\frac{1+T Y^{-N}}{(1+T)^3}.
 \tag{11}
\]
The difference of the two sides in (9) is therefore a single
integral:
\[
 X_E F
   =-iN\int_{-1}^{h_x}
       D_N(s,y)f_N(a_N+is,y;u)\,ds,
 \tag{12}
\]
where
\[
 \boxed{\displaystyle
 D_N(s,y)=
 \frac{T^2(Y^{-N}-3-3T-T^2)}{(1+T)^4}.}
 \tag{13}
\]
In (12), \(F\) denotes the original \(x\)-input (3).
There is no estimate in this calculation. In particular,
the factor \(Y^{-N}\) has been retained.

When \(y=j/N\), that factor equals one. When the subsequent
\(y\)-residue identity is applied, its input is the entire
holomorphic product
\[
                   D_N(s,y)f_N(a_N+is,y;u).
 \tag{14}
\]
It would be incorrect to replace \(Y^{-N}\) by one on the
complex contour merely because it equals one on the grid.

## 4. The exact sixteen-term assembly

Call the four \(x\)-terms \(X_U,X_+,X_-,X_E\), with \(X_E\)
in its combined form (12). For each fixed point of these
terms apply the four \(y\)-operators \(Y_U,Y_+,Y_-,Y_E\)
on \([c_N,d_N]\), with upper height \(v(\Im x)\) and
lower height \(-h_y\).

Then (2) is exactly the sum of the sixteen resulting
iterated integrals. For the combined term this means
\[
 -iN\int_{-1}^{h_x}
 (Y_U+Y_++Y_-+Y_E)
       [D_N(s,\cdot)f_N(a_N+is,\cdot;u)]\,ds .
 \tag{15}
\]
All other terms use (3) directly.
This formula has only the two actual \(y\)-endpoints
\(c_N,d_N\). There are no diagonal endpoints, staircase
corners, or moving upper limits of a row.

The principal term is
\[
 N^2\int_{a_N}^{b_N}\int_{c_N}^{d_N}
           f_N(x+ih_x,y+ih_y;u)\,dy\,dx .
 \tag{16}
\]
Its stationary point is the original finite critical point.
On the full upper rectangle the canonical upper-half-plane
primitive of \(J\) continues across \(\Re(x+y)=1\).
The exact factorial has no pole there. Its continued
asymptotic is proved uniformly in
[the half-plane continuation lemma](research_factorial_uniform_halfplane_continuation.md).
That lemma and the proved horizontal maximum therefore
apply also to the zero-extended part of the rectangle.

## 5. All four lower-\(x\) terms are already negligible

For \(X_-\), \(x\) traverses the complete interval
\([a_N,b_N]\) at height \(-1\).
The \(y\)-contours have upper height \(h_a\), lower height
\(-h_y\), and their kernels are independent of \(\Re x\).
One may therefore integrate in \(x\) first at every fixed
point of every \(y\)-contour.

The [full-circle theorem](research_adjacent_pair_full_circle_bound.md)
proves a uniform negative exponential bound for that integral.
It uses the exact cyclic gauge, whose normalized one-form
is holomorphic at \(w=0\), and bounds the exponentially small
error of returning to the original normalization.
It applies to \(Y_U,Y_+,Y_-\), and \(Y_E\) together,
including all lower Fourier modes and the vertical
\(y\)-endpoints. Thus none of the four \(X_-\) terms
requires an individual absolute phase estimate.

## 6. The rate for the combined sides

Let \(t=\Im y\). The exact expression (13) gives
\[
 |D_N(s,y)|\le
  8\exp\{N\mathcal E(s,t)\},
 \tag{17}
\]
where
\[
\begin{aligned}
 \mathcal E(s,t)
   &=4\pi s+\max(2\pi t,0,2\pi s,4\pi s)
                          -8\pi\max(s,0)\\
   &=
    \begin{cases}
      4\pi s+2\pi\max(t,0),&s\le0,\\
      \max(2\pi t-4\pi s,0),&s\ge0.
    \end{cases}
\end{aligned}
\tag{18}
\]
The variable \(t\) in (18) is an imaginary height, not the
positive quantity \(T=e^{2\pi Ns}\) in (13).

Consequently the three basic grouped phase bounds to check
at \(u=0\) are
\[
\begin{aligned}
 F_U(a,s)&=\Re W(is,a+i v(s))+\mathcal E(s,v(s)),\\
 F_L(a,s)&=\Re W(is,a-ih_y)+\mathcal E(s,-h_y)-2\pi h_y,\\
 F_E(b,s,t)&=\Re W(is,b+it)+\mathcal E(s,t)-2\pi(-t)_+ .
\end{aligned}
\tag{19}
\]
Their domains are respectively
\[
\begin{gathered}
 c_N\le a\le d_N,\quad -1\le s\le h_x,\\
 b\in\{c_N,d_N\},\quad -1\le s\le h_x,\quad
                              -h_y\le t\le v(s).
\end{gathered}
\tag{20}
\]
For \(X_EY_+\) there is the additional penalty \(2\pi v(s)\);
a bound for \(F_U\) therefore suffices.

Here \(W(is,y)\) denotes the continuous limiting real phase
at the left side. It is the appropriate uniform finite-\(N\)
upper exponent, not a replacement of a finite endpoint.
Indeed \(Nx=-1/2+iNs\) exactly. The midpoint estimate in
the uniform factorial note applies to
\[
 G_N(Nx)=G_N(N(is)-1/2),\qquad
 G_N(N(x+y))=G_N(N(y+is)-1/2).
 \tag{21}
\]
It includes \(s=0\), where an ordinary interior Stirling
estimate would be insufficient. The remaining factorials
have regular real parts; the explicit exponential in (3)
changes by a uniformly bounded factor when
\(x=-1/(2N)+is\) is replaced by \(is\) in its leading
phase. Thus (19) has a uniform polynomial prefactor
through the whole interval of \(s\).

For arbitrary real boundary angles, the uniform Newton
inequality adds a positive multiple of \(1-\cos u\) to the
loss in (19). It retains the original midpoint shifts
and all reciprocal-factorial zero faces.

## 7. Completion of the source theorem

The rectangle identity and the full-circle bound remove
the former diagonal-corner obstruction. The
[grouped contour inequalities](research_adjacent_pair_grouped_contour_bounds.md)
now prove a fixed gap below the selected rate for the three
functions (19), on their entire domains, together with the
upper-\(x\) correction and \(y\)-endpoint integrals.
Their proof includes the actual cutoff and half-grid
endpoints. The principal term (16) is handled by the
full-rectangle horizontal maximum and nondegenerate
stationary phase.

These inputs give the
[nonzero local asymptotic and full boundary bounds](research_adjacent_two_crossing_boundary_theorem.md)
for the whole original boundary polynomial; the discarded
\(j\)-tails are already exponentially smaller. The
rectangle extension has not changed an invariant or
a trace. It has only made the exact relation between
the two \(x\)-sides available before taking absolute
values.
