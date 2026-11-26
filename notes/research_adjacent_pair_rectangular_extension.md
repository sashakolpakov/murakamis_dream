# Extending the adjacent-pair source to a rectangular sum

Research note, 2 November 2026.

The exact adjacent-pair source is written as a sum over
\(i,j\ge0\), \(i+j<N\). Its canonical factorial interpolation
extends holomorphically to a neighborhood of the full square
\(0\le i,j<N\). Every added lattice term is exactly zero.
This removes the diagonal staircase from the finite summation
domain without changing the boundary polynomial.

The assertion is about the exact finite-level functions.
Uniform asymptotic estimates for a contour crossing the
diagonal remain a separate matter.

## 1. The divisor of the canonical factorial

Use the canonical factorial and its Gamma product from
[the exact factorial note](research_exact_cyclotomic_factorial.md):
\[
 G_N(z)=\left(\frac{2\pi}{N}\right)^z\Gamma(z+1)
 \prod_{m\ge1}
 \frac{\Gamma(Nm+z+1)}
      {\Gamma(Nm-z)(Nm)^{2z+1}}.
 \tag{1}
\]
All powers of positive numbers use their real logarithms.

**Lemma 1.** The product defines a meromorphic function on
\(\mathbb C\). It has no zeros or poles away from the
integers, and at every integer \(k\),
\[
 \operatorname{ord}_{z=k}G_N(z)=\left\lfloor\frac{k}{N}\right\rfloor.
 \tag{2}
\]
Positive order denotes a zero and negative order a pole.

**Proof.** On a fixed compact set, sufficiently large factors
are nonzero and their logarithms are uniformly \(O(m^{-2})\),
by the same Gamma-ratio expansion used to define (1).
Their product therefore converges normally to a nonzero
holomorphic function. All divisors come from the finitely
many remaining Gamma factors.

For \(k\ge0\), neither \(\Gamma(k+1)\) nor
\(\Gamma(Nm+k+1)\) has a pole. A reciprocal denominator
\(1/\Gamma(Nm-z)\) has a simple zero at \(z=k\) precisely
when \(Nm\le k\). There are \(\lfloor k/N\rfloor\) such
factors.

For \(k=-r<0\), the initial factor \(\Gamma(z+1)\)
has one simple pole. The numerator \(\Gamma(Nm+z+1)\)
has a simple pole precisely when \(Nm\le r-1\);
the denominator is finite and nonzero. The total pole
order is
\[
 1+\left\lfloor\frac{r-1}{N}\right\rfloor
       =\left\lceil\frac rN\right\rceil
       =-\left\lfloor\frac{-r}{N}\right\rfloor.
 \]
There are no other Gamma poles, and Gamma has no zeros.
This proves (2). QED.

In particular, \(G_N\) is holomorphic on \(\Re z>-1\),
and \(1/G_N\) is holomorphic on \(\Re z<N\), with its
removable values at the negative integer poles.

**Corollary 2.** For \(N\le k\le2N-2\), the zero at \(k\)
is simple. Writing \(k=N+r\), \(0\le r\le N-2\), its
derivative is
\[
 G_N'(N+r)=-2\pi(-1)^r S_r,\qquad
 S_r=\prod_{\ell=1}^r2\sin(\pi\ell/N).
 \tag{3}
\]
Indeed the exact period relation is
\[
 G_N(z+N)=-2\sin(\pi z)G_N(z).
 \tag{4}
\]
Differentiate at \(z=r\), where \(G_N(r)=S_r\ne0\).

## 2. The source is holomorphic on a tube around the square

Put \(D=N-1\), \(s=u/(2\pi)\), and use the exact interpolation
from [the cyclotomic calculation](research_adjacent_pair_cyclotomic_gauge.md):
\[
 \mathcal B_N(y,u)=
 \frac{G_N(D/2+Ns)G_N(D/2-Ns)}
 {G_N(D/2-Ny+Ns)G_N(D/2-Ny-Ns)G_N(Ny)^2},
 \tag{5}
\]
\[
 \begin{split}
 f_N(x,y;u)={}&N^2
 \exp\left\{i\pi N(x^2-xy+y^2/2+x+y/2)
                         -i\pi(x+y/2)\right\}\\
 &\times
 \frac{G_N(N(x+y))}{G_N(Nx)^3G_N(Ny)^2}
                         \mathcal B_N(y,u).
 \end{split}
 \tag{6}
\]
Whenever a denominator \(G_N\) has a pole, the corresponding
reciprocal in (5)--(6) is interpreted by its holomorphic
extension.

**Proposition 3.** The function (6) is holomorphic on the
following tube:
\[
 -\frac1{4N}<\Re x,\Re y<1-\frac3{4N},
 \qquad |\Re s|<\frac18.
 \tag{7}
\]
In particular this tube contains every lattice point
\((i/N,j/N)\), \(0\le i,j<N\), and crosses
\(\Re(x+y)=1\).

**Proof.** The arguments \(Nx,Ny\) have real parts between
\(-1/4\) and \(N-3/4\); the denominator factors in (6)
are nonzero and holomorphic there. The numerator
\(N(x+y)\) has real part greater than \(-1/2\), so
Lemma 1 shows that its factorial is holomorphic.
Its integer zeros are harmless.

The numerator arguments in (5) have real parts between
\(3N/8-1/2\) and \(5N/8-1/2\), which lie in \((0,N)\)
for every \(N\ge2\). The real parts of its two shifted
denominator arguments lie between
\[
 -5N/8+1/4\quad\hbox{and}\quad5N/8-1/4.
 \]
They are strictly between \(-N\) and \(N\).
The reciprocals of their factorials are holomorphic
throughout this strip by Lemma 1. Thus their negative
integer poles can only produce zeros of (5), not a
hidden singularity of (6). All other factors are entire.
QED.

No restriction on the imaginary parts is needed for this
finite-\(N\) holomorphy statement.

The actual residue contours use half-grid endpoints rather
than just a neighborhood of the lattice. Their holomorphy
also follows directly.

**Corollary 3a.** Fix \(0<\epsilon<1/2\). The source is
holomorphic on an open neighborhood of every finite-height
part of the slab
\[
 -\frac1{2N}\le\Re x\le1-\frac1{2N},\qquad
 \frac{\epsilon}{2}\le\Re y\le\frac12-\frac{\epsilon}{2},
 \qquad -\pi\le\Re u\le\pi.
 \tag{7a}
\]
The imaginary parts of \(x,y,u\) may range over arbitrary
fixed bounded intervals. Thus the statement includes the
full real boundary period, a thin complex strip in that
period, and the endpoint perturbations of the truncated
\(y\)-interval for all sufficiently large \(N\).

**Proof.** The exact reflection identity
\[
 G_N(z)G_N(N-1-z)=N
 \]
reduces the numerator of (5) identically to \(N\), with
any apparent singularities removed. This identity follows
from the finite logarithmic derivative; its short proof is
given in [the boundary-order note, Section 1](research_balanced_factorial_boundary_order.md).

The reciprocals \(1/G_N(Nx)\), \(1/G_N(Ny)\) are holomorphic
because their arguments have real part less than \(N\).
The two shifted reciprocal factorials in (5) also have real
part at most
\[
 N(1-\epsilon/2)-1/2<N.
 \]
Finally,
\(\Re N(x+y)\ge-1/2+N\epsilon/2>-1\), so its numerator
factorial is holomorphic. These inequalities are strict
and therefore persist on an open neighborhood of any
finite-height compact part of the slab. QED.

The positive lower bound on \(\Re y\) matters here. A
product contour with both lower real endpoints equal to
\(-1/(2N)\) would pass through
\(N(x+y)=-1\), a pole of the numerator factorial.
Corollary 3a concerns the actual truncated \(y\)-interval,
whose real endpoints stay away from zero.

## 3. Exact lattice values outside the triangle

Iteration of the factorial recurrence gives, at \(y=j/N\),
\[
 \mathcal B_N(j/N,u)=
 \frac1{S_j^2}
 \prod_{\ell=0}^{j-1}
   \left(2\cos\frac{\pi(2\ell+1)}N+2\cos u\right)
 =e_j(-2\cos u).
 \tag{8}
\]
This is an identity of meromorphic expressions and hence
also of their removable continuations. The right-hand side
is the original Newton polynomial evaluated at the retained
boundary angle.

**Theorem 4.** The entire original boundary polynomial has
the exact rectangular expression
\[
 \boxed{
 Z_N(u)=\sum_{i=0}^{N-1}\sum_{j=0}^{N-1}
                    f_N(i/N,j/N;u).}
 \tag{9}
\]
Every summand with \(i+j\ge N\) is zero for all \(u\) on
the parameter neighborhood (7), and hence under its entire
continuation.

**Proof.** At the retained lattice points \(i,j<N\), the
factors \(G_N(i)=S_i\), \(G_N(j)=S_j\) are nonzero.
Equation (8) is finite. When \(N\le i+j\le2N-2\),
Corollary 2 gives \(G_N(i+j)=0\). Proposition 3 excludes
any opposing pole. Thus the added summands vanish exactly.
Inside the triangle, (6) is the original exact summand.
This proves (9). Since the zero summands vanish identically
in \(u\), all their derivatives in the retained boundary
parameter vanish as well. QED.

The factorial zero is simple, not infinitely flat in the
summation coordinates. Near an exterior lattice point with
\(k=i+j\), the numerator is
\[
 G_N(N(x+y))
   =N G_N'(k)\left(x+y-\frac{k}{N}\right)
       +O\!\left(\left(x+y-\frac{k}{N}\right)^2\right).
 \tag{10}
\]
Its derivative is fixed by (3). The remaining factor can
vanish too, for example at a folded Newton zero. Nothing
in the rectangular extension discards these analytic
derivatives or asserts that the source vanishes in an
open neighborhood of the added lattice points.

Likewise, the product lattice kernel
\[
 \frac{f_N(x,y;u)}
 {(e^{2\pi iNx}-1)(e^{2\pi iNy}-1)}\,dx\,dy
 \tag{11}
\]
can still have single-divisor poles at an exterior lattice
point. Its double residue there is zero because the source
value is zero. Holomorphy of \(f_N\) must not be confused
with holomorphy of the two-variable residue kernel.

## 4. Translation and passage across the diagonal

The exact \(x\)-translation identity remains
\[
 \frac{f_N(x+1,y;u)}{f_N(x,y;u)}
 =\frac{U^2(UV-1)}{V(U-1)^3},\qquad
 U=e^{2\pi iNx},\quad V=e^{2\pi iNy},
 \tag{12}
\]
as an identity of meromorphic functions. It follows from
(4) and the original exponential in (6), independently of
whether \(\Re(x+y)\) is below or above one.

The ratio in (12) is not to be evaluated by substituting
\(U=V=1\) at lattice points. It can have poles, and
translating \(x\) by one leaves the tube (7). Neither fact
affects the original rectangular sum, which does not
translate its indices.

On an upper contour with \(\Im x,\Im y>0\), both
\(|U|,|V|<1\). The same ratio can be written as
\[
 \frac{U^2}{V}\,
                 \frac{1-UV}{(1-U)^3}.
 \tag{13}
\]
It is nonzero there. Crossing \(\Re(x+y)=1\) at positive
imaginary height meets no factorial zero, and no new
singularity of (6) appears.

The lower-disk power-series logarithm used in the
cyclotomic normalization applies only to
\(|w|<\min(1,|Y|)\), where
\(w=e^{-2\pi ix}\), \(Y=e^{2\pi iy}\).
It is not a logarithm that can be reused on an upper
contour without continuation. The rational identity
(12) is global; that particular logarithmic expansion
is local.

Consequently the diagonal staircase is unnecessary at
the exact finite level. The next analytic task is to
estimate the extended summand on the chosen rectangular
contours, using the appropriate branches and all connecting
faces. Proposition 3 supplies holomorphy for that task;
it supplies no exponential bound by itself.
