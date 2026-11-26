# Exact strip reconstruction on every compact positive angle triangle

Private written proof, 18 November 2026.

The actual balanced Gauss polynomial has a single cardinal projection
of an exact factorial ratio. Pairing the two sides of a width-one strip
gives an explicit boundary current with both Fermat numerators. The
current is polynomially bounded on the real scalar torus, uniformly on
a scaled meridian disk. Consequently the exact ratio is the selected,
nonzero asymptotic throughout every compact positive angle triangle,
including a fixed complex neighborhood and fixed normal derivatives.

This is a scalar reconstruction theorem for the polynomial in complete
direct C. Its Laurent-polynomial evaluation on the actual Cartan and
Casimir, its Jordan data, exterior coupons, and source functional are
still the ones in C. No operator norm, coherent-kernel estimate, or
geometric source coefficient is inferred from this scalar theorem.

## 1. Exact functions and the theorem

Put
\[
 c_0=2\pi i,\quad Q=e^{c_0/N},\quad d=N-1,\qquad
 c=e^{c_0(1+\beta)/N},\quad \rho=e^{c_0\beta}=c^N.
 \tag{1}
\]
The root is fixed. The physical scaled meridian is
\(M=e^{\xi/N}\), with \(\beta=-2\xi/c_0\). Fix a sufficiently
small disk \(|\beta|\le\beta_0<1/4\), and enlarge it slightly
whenever Cauchy estimates are used.

Use F's exactly normalized factorial \(\widehat F_N\), denoted by
\(F_N\) in this note. Its proved identities are
\[
 \begin{split}
 F_N(z+1)&=(1-Q^{z+1})F_N(z),&F_N(0)&=1,\\
 F_N(z+N)&=(1-e^{c_0z})F_N(z),\\
 F_N(z)F_N(d-z)&=N e^{i\pi z(z-d)/N}.
 \end{split}\tag{2}
\]
The second identity follows by multiplying the first \(N\) times.
The function is holomorphic and nonzero on \(-1<\Re z<N\),
and continues holomorphically to \(\Re z>-1\) by the first
identity. Its further zeros cause no numerator poles below.

For \(A=e^{c_0x}\), \(B=e^{c_0y}\), define the exact ratio
\[
 \mathcal B_{N,\beta}(x,y)=
 \frac{F_N(N(x+y)+\beta)F_N(\beta)}
 {F_N(Nx+\beta)F_N(Ny+\beta)}.
 \tag{3}
\]
Let \(\mathcal S_N(A,B;c)\) be C's literal degree-at-most-\(d\)
polynomial in each scalar argument. The precise conclusion is:

**Theorem.** For every compact set
\[
 K\Subset\{(x,y)\in\mathbb R^2:x>0, y>0, x+y<1\},
 \tag{4}
\]
there is a fixed complex neighborhood \(U\) of \(K\), and
\(\epsilon>0\), such that
\[
 \boxed{\quad
 \mathcal S_N(e^{c_0x},e^{c_0y};c)
 =\mathcal B_{N,\beta}(x,y)
                  \bigl(1+O(e^{-\epsilon N})\bigr).
 \quad}\tag{5}
\]
The estimate is uniform on \(U\times\{|\beta|\le\beta_0\}\),
after shrinking the disk if necessary. Every fixed derivative of the
normalized error has the same exponential bound on smaller domains.
In particular the reconstructed scalar is nonzero there for large \(N\).

Here is its calibrated leading term. On the logarithmic strip set
\[
 I(z)=\frac{\operatorname{Li}_2(1)-
                   \operatorname{Li}_2(e^{c_0z})}{c_0},
 \qquad \Phi(x,y)=I(x+y)-I(x)-I(y),
 \tag{6}
\]
with continuation from the real interval \(0<z<1\). Also put
\[
 \Lambda(x,y)=\frac{\pi\sin\pi(x+y)}
                         {\sin\pi x\sin\pi y}.
 \tag{7}
\]
The powers and square root are continued from their positive real
values on the triangle. Uniformly on a smaller \(U\),
\[
 \boxed{\quad
 \mathcal S_N=
 \frac{\Gamma(1+\beta)N^{-\beta}\Lambda(x,y)^\beta}
      {\sqrt{2N}}
 \sqrt{\frac{\sin\pi(x+y)}{\sin\pi x\sin\pi y}}
 e^{N\Phi(x,y)}\bigl(1+O(N^{-1})\bigr).
 \quad}\tag{8}
\]
This proves reconstruction for arbitrary compact strict triangles,
not only for a neighborhood of the entropy maximum.

## 2. One cardinal projection, with the original coefficients

Write \(g_j=(c;Q)_j\) and
\(L_k(B)=N^{-1}\sum_{j=0}^d(BQ^{-k})^j\). C proves
\[
 \mathcal S_N(A,B;c)=
 \sum_{l,k=0}^d\frac{g_{l+k}}{g_lg_k}L_l(A)L_k(B).
 \tag{9}
\]
For each integer \(0\le k<N\), (2) gives exactly
\[
 \mathcal B_{N,\beta}(x,k/N)
                  =\frac{(cA;Q)_k}{(c;Q)_k}.
 \tag{10}
\]
This is a polynomial of degree at most \(k\) in \(A\), whose
values at \(A=Q^l\) are the coefficients in (9). Therefore
\[
 \boxed{\quad
 \mathcal S_N(A,B;c)=
       \sum_{k=0}^d L_k(B)\mathcal B_{N,\beta}(x,k/N).
 \quad}\tag{11}
\]
This identity is whole-meridian. In particular it does not delete
the upper triangle before differentiation. No approximate sampling
or interpolation in an occupation index has occurred.

Use the cardinal kernel
\[
 \mathcal K_N(y,w)=
 \frac{c_0(B^N-1)}
 {(e^{c_0Nw}-1)(e^{c_0(y-w)}-1)}.
 \tag{12}
\]
Its residue at \(w=k/N\) is \(L_k(B)\); its residue at
the source pole \(w=y\) is \(-1\). It is one-periodic in \(w\).
Source values coinciding with a grid point will always be obtained
by holomorphic continuation of the final identities.

Fix \(a=1/2\). For sufficiently large \(N\), the strip
\[
             -a/N<\Re w<1-a/N
 \tag{13}
\]
contains exactly the grid \(0,1/N,\ldots,d/N\) and one source
pole for \(y\) in any fixed compact substrip of \(0<\Re y<1\).
The denominator arguments \(Nw+\beta\) remain in the zero-free
strip of \(F_N\), since \(|\Re\beta|<1/4\). The numerator
argument has positive real part if \(x\) is in a compact substrip
and \(N\) is large. It can cross \(N\), where it can have zeros,
but it has no poles. Thus the only poles of the integrand in (13)
are the stated cardinal and source poles.

Integrate \(\mathcal K_N(y,w)\mathcal B_{N,\beta}(x,w)\)
on the positively oriented rectangle obtained by cutting (13)
at imaginary heights \(\pm T\). The two horizontal ends tend
to zero as \(T\to\infty\), for each fixed \(N\). A proof of
this assertion, including the lower end, is given in Section 3.
Pair the remaining vertical sides by \(w\mapsto w+1\). From (2),
\[
 \mathcal B_{N,\beta}(x,w+1)
  =\frac{1-\rho A^N e^{c_0Nw}}{1-\rho e^{c_0Nw}}
                         \mathcal B_{N,\beta}(x,w).
 \tag{14}
\]
The right side of the rectangle is upward, and the left side is
downward. The residue theorem and (14) give the exact current
\[
 \boxed{\begin{split}
 \mathcal S_N(A,B;c)-\mathcal B_{N,\beta}(x,y)
   ={}&\frac{1-A^N}{2\pi i}
       \int_{\Re w=-a/N}^{\uparrow}
       \mathcal K_N(y,w)
       \frac{\rho e^{c_0Nw}}{1-\rho e^{c_0Nw}}
                  \mathcal B_{N,\beta}(x,w)\,dw.
 \end{split}}\tag{15}
\]
Both Fermat factors remain: the other is \(B^N-1\) in (12).
In particular the infinity cancellation is between two actual sides
of one strip; neither side is independently discarded.

## 3. Uniform factorial estimates on complete vertical strips

We record the uniformity needed in (15), directly from F's convergent
Gamma product. For fixed \(b>0\), \(\delta>0\), uniformly on
\[
                 b/N\le\Re z\le1-\delta,
                  \qquad \Im z\in\mathbb R,
 \tag{16}
\]
one has, with the same logarithmic marks as F,
\[
 F_N(Nz)=\sqrt{iN(1-e^{c_0z})}\,e^{NI(z)}e^{O_{b,\delta}(1)}.
 \tag{17}
\]
The \(O(1)\) is a bound for a holomorphic logarithmic error, and
therefore bounds the reciprocal as well. If the real part is also
bounded below by a fixed positive constant, the error in (17)
can be replaced by
\(\pi\cot(\pi z)/(12N)+O(N^{-3})\), uniformly for all imaginary
heights.

For precision, apply Stirling through its \(1/(12Z)\) term to
F's Gamma arguments \(Nz\), \(N(k+z)\), and \(N(k-z)\).
Their real parts are positive. The remainder is bounded by
\(C|Z|^{-3}\) throughout the closed right half-plane, as follows
from the integral Bernoulli remainder used in F. The first remainder
is at most \(Cb^{-3}\); the sum of the others is bounded by
\[
 CN^{-3}\sum_{k\ge1}
    \bigl((k+b/N)^{-3}+(k-1+\delta)^{-3}\bigr).
 \tag{18}
\]
These estimates are independent of \(\Im z\). The same sine-product
summation as in F gives \(NI(z)\), the marked half logarithm, and
\(\pi\cot(\pi z)/(12N)\). Since
\(|\cot\pi z|\le C_{\delta}(1+1/\Re z)\), the last term is
bounded on (16). This proves (17). On a fixed smaller vertical
strip every remainder is \(O(N^{-3})\), proving the stronger
assertion. Thus no compact-height estimate has been used at
unbounded height.

For \(\beta\) in the stated disk the same product at bounded
argument gives
\[
 F_N(\beta)=(-c_0/N)^\beta\Gamma(1+\beta)
                                      (1+O(N^{-1})),
 \qquad \Log(-c_0)=\log(2\pi)-i\pi/2.
 \tag{19}
\]
For example the logarithm of the infinite Gamma-product correction
is \(O(N^{-2})\) uniformly on this disk; the explicit Gaussian
factor has a uniform \(O(N^{-1})\) correction. In particular this
factor and its reciprocal have polynomial size in \(N\).

Here also is the promised horizontal-end justification. On a fixed
real substrip of the basic factorial strip, (17), with its bounded
reciprocal, shows that \(F_N(z)\) and \(F_N(z)^{-1}\) are bounded
as \(\Im z\to+\infty\), for fixed \(N\). This follows because
\(e^{c_0z/N}\to0\), so both the displayed square root and \(I\)
have finite limits. Literal shifts in (2) give the same conclusion
on each bounded real interval needed for numerator arguments.
Near the left edge, shift once before using (17); the shift factor
tends to one. Consequently \(\mathcal B(x,w)\) is bounded at
the upper horizontal end, whereas \(\mathcal K(y,w)=O_N(e^{-2\pi T})\).

At the lower end use the reflection in (2), and these upper bounds
and reciprocal bounds. For \(w=t-iT\), uniformly over the fixed
real interval in (13), it gives
\[
 |\mathcal B_{N,\beta}(x,w)|
       \le C_{N,x,\beta}e^{2\pi N(\Re x)T},
 \qquad |\mathcal K_N(y,w)|\le C_{N,y}e^{-2\pi NT}.
 \tag{20}
\]
Indeed the ratio of the two reflected quadratic exponentials is
a constant times \(e^{c_0Nxw}\); the remaining upper-height
factorial ratios are bounded. Since \(\Re x<1\), this end also
vanishes. These are fixed-\(N\) end limits establishing the exact
current. The uniform estimate for that current is proved next.

## 4. The paired current has polynomial size

Let \(x,y\) range in arbitrary fixed compact subsets of
\(0<\Re x,\Re y<1\). We claim that there are constants \(C,p\)
independent of \(N\) such that
\[
 \boxed{\quad
 |\mathcal S_N(A,B;c)-\mathcal B_{N,\beta}(x,y)|
       \le CN^p|1-A^N|\,|1-B^N|.
 \quad}\tag{21}
\]
This bound holds wherever (3) is defined; numerator zeros are harmless.
Only sufficiently large \(N\) is required on the fixed compacts.

First prove the necessary estimate on the left side. Put
\[
 w=(-a+iv)/N,\qquad z=w+(\beta+1)/N.
 \tag{22}
\]
Then \(\Re z\in[1/4,3/4]/N\). A single factorial shift gives
exactly
\[
 \mathcal B_{N,\beta}(x,w)=
 \frac{F_N(N(x+z))}{F_N(Nz)}
 \frac{1-e^{c_0z}}{1-e^{c_0(x+z)}}
 \frac{F_N(\beta)}{F_N(Nx+\beta)}.
 \tag{23}
\]
All the denominator factors in this formula are nonzero on the
stated domains. Apply (17) to \(z,x+z,x+\beta/N\), and (19).
The half-logarithms in (23) combine into a bounded multiple of
\[
 N^{-1/2}|F_N(\beta)|
 \left|\frac{1-e^{c_0z}}
 {(1-e^{c_0(x+z)})(1-e^{c_0(x+\beta/N)})}\right|^{1/2}.
\]
This is polynomially bounded uniformly for all real \(v\). The
ratio involving \(z\) is bounded also at large negative height,
where its numerator and denominator have the same exponential
growth; the real part of \(x+z\) stays away from both strip edges.
Since \(N(I(x+\beta/N)-I(x))=O(1)\), it follows that
\[
 |\mathcal B_{N,\beta}(x,w)|
               \le CN^p e^{N\Re\Phi(x,z)}.
 \tag{24}
\]

The endpoint displacement in (22) costs only \(O(\log N)\) in
the exponent, uniformly for all \(v\):
\[
 N|\Phi(x,z)-\Phi(x,iv/N)|\le C(1+\log N).
 \tag{25}
\]
To see this, use
\(\partial_z\Phi=\Log(1-e^{c_0(x+z)})-
\Log(1-e^{c_0z})\). First move horizontally from \(iv/N\)
to \(r+iv/N\), \(r=\Re z\), then vertically by
\(i\Im\beta/N\). Near zero the only singularity is an
integrable logarithm; its integral over a segment of length \(O(1/N)\)
is \(O((1+\log N)/N)\), uniformly in the starting height.
On bounded sets away from zero the derivative is bounded. At large
positive height both logarithms tend to zero. At large negative
height their linearly growing logarithms cancel, and their difference
tends to \(c_0x\), uniformly on the compact \(x\)-set. This proves
(25), including \(|v|\gg N\); bounding the two large logarithms
separately would not prove it.

There is a strict argument gap for the remaining phase. Choose
\(\delta>0\) with \(\delta\le\Re x\le1-\delta\).
For every \(r>0\), the strip branch satisfies
\[
 -\pi+2\pi\delta\le
       \Arg(1-r e^{c_0\Re x})\le\pi-2\pi\delta.
 \tag{26}
\]
For \(t>0\), taking the boundary value from \(\Re z>0\),
\[
 \partial_t\Re\Phi(x,it)
       =-\Arg(1-e^{c_0x}e^{-2\pi t}).
\]
For \(t<0\) the denominator logarithm has argument \(-\pi\),
so the same derivative is the preceding expression minus \(\pi\).
Since \(\Phi(x,0)=0\), integration gives
\[
                 \Re\Phi(x,it)\le(2\pi-2\pi\delta)|t|.
 \tag{27}
\]
This uses only the real part of \(x\) in (26); its imaginary part
changes the positive modulus \(r\). Combining (24)--(27), for
some fixed \(\epsilon_0>0\),
\[
 |\mathcal B_{N,\beta}(x,(-a+iv)/N)|
             \le CN^p e^{(2\pi-\epsilon_0)|v|}.
 \tag{28}
\]

On this line \(V=e^{c_0w}\) has
\(V^N=-e^{-2\pi v}\). For the small \(\beta\)-disk,
\[
 \left|\frac{\rho V^N}{(V^N-1)(1-\rho V^N)}\right|
                              \le C e^{-2\pi|v|}.
 \tag{29}
\]
Also \(B/V-1\) is uniformly bounded away from zero: the argument
of \(B/V\) is \(2\pi(\Re y+a/N)\), a fixed distance from
\(2\pi\mathbb Z\). The modulus of \(B/V\) can vary with \(v\)
without spoiling this lower bound.
Substitute (28)--(29) in (15), with \(|dw|=dv/N\).
The remaining integral is bounded by
\(C\int_{\mathbb R}e^{-\epsilon_0|v|}\,dv\).
This proves (21), absolute convergence of the paired current, and
local holomorphy in all scalar and scaled meridian parameters.

## 5. The positive triangle and the selected coefficient

On a compact complex subdomain with \(x,y,x+y\) in the strip,
F's uniform expansion and (19) give
\[
 F_N(Nx+\beta)=
   \sqrt{iN(1-e^{c_0x})}\,
   (1-e^{c_0x})^\beta e^{NI(x)}(1+O(N^{-1})).
 \tag{30}
\]
Insert (30) and (19) into (3). The identity
\[
 (-c_0)\frac{1-e^{c_0(x+y)}}
 {(1-e^{c_0x})(1-e^{c_0y})}=\Lambda(x,y)
\]
and the marked square roots give precisely the leading term in (8)
for the exact ratio, with a nonzero amplitude.

For real \(0<x,y,x+y<1\), write
\(J(t)=\int_0^t\log(2\sin\pi s)\,ds\). Then
\[
 \Re\Phi(x,y)=H(x,y):=J(x+y)-J(x)-J(y)>0,
 \qquad \Im\Phi(x,y)=\pi xy.
 \tag{31}
\]
For completeness, \(H\) is zero on the three boundary edges:
\(J(1)=0\) and \(J(1-t)=-J(t)\). Its Hessian has negative
first diagonal entry
\(\pi(\cot\pi(x+y)-\cot\pi x)\) and determinant \(\pi^2\).
It is strictly concave in the triangle. Strict positivity in (31)
follows by comparing an interior point with the endpoints of a
boundary-to-boundary segment through it.

Thus \(H\) has a positive minimum on \(K\). Choose a fixed complex
neighborhood \(U\) sufficiently small that \(\Re\Phi\) remains
positive and
\[
 2\pi\{(-\Im x)_++(-\Im y)_+\}<\tfrac12\Re\Phi(x,y)
                                                        \quad\hbox{on }U.
 \tag{32}
\]
The two Fermat factors in (21) are bounded by
\(4\exp(2\pi N\{(-\Im x)_++(-\Im y)_+\})\).
The amplitude of (3) and its reciprocal are polynomially bounded
on \(U\times\{|\beta|\le\beta_0\}\). Equations (21),(30)--(32)
give (5), with a fixed exponential relative gap. The coefficient
of the exact ratio is \(+1\), fixed by the source-pole residue in
(12), not chosen by a saddle or by a positive replacement array.

At grid source values the contour formula was initially obtained by
separating poles. Both sides of (15) extend holomorphically, and the
paired integral is uniformly convergent on the compact scalar domains.
Thus (15), (21), and (5) continue to those values as well. Cauchy on
slightly larger fixed neighborhoods gives all stated derivatives of
the normalized errors.

## 6. Actual normals and the remaining source question

The entire proof keeps \(c=M^{-2}Q\) before specialization. On the
root, at fixed \(x,y\), the true \(\mu=\Log M\) derivative is
\[
 \left.\partial_\mu\Log\mathcal S_N\right|_{\mu=0}
  =\frac{2N}{c_0}
       \{\log N+\gamma_E-\Log\Lambda(x,y)\}+O(1).
 \tag{33}
\]
Indeed \(\partial_\mu=-(2N/c_0)\partial_\beta\), and
\(\Gamma'(1)=-\gamma_E\). Fixed higher scaled normal derivatives
of the relative reconstruction error are exponentially small; converting
to fixed \(\mu\)-derivatives introduces the corresponding powers of
\(N\). No moving-root normal is asserted.

C's upper-carry array and its first normal have not been omitted: they
are present in (9)--(11), and therefore in the exact strip current.
Likewise (15) explicitly retains the infinity complement through its
paired sides. A fixed-height estimate of just one side could have the
positive rate \(-\Re I(x)\); it is (14) and the orbit weight (29)
that prove the cancellation needed here.

For the actual operator one still has C's ordered evaluation
\(\mathcal A_N=H_dK^d\mathcal S_N(u,v;c)\), symmetric in
\(u,v\), followed by its original routed factors and source closure.
This note does not replace those commuting matrix/Jordan arguments by
arbitrary scalar \(x,y\), bound their conditioned evaluation, or put
a geometric opposite-polarization kernel into \(U\). Moving arguments,
the outer \(H_dK^d\), quotient, turnover, central normalization, pivots,
and marks retain all their own normal terms. A nonzero scalar coefficient
on this fixed chart is not a nonzero original closed source.

## Complete proof directs

* C: notes/research_balanced_gauss_cyclic_divisor_source.md,
  SHA256 c15668d7dff95346d72801b721bf95970b661e5b17d125aaadd7e0dc38905b00.
* F: notes/exact_factorial_interpolation_and_complex_contours.md,
  SHA256 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.

Both complete directs and the entire final were read nontruncated in
this author sequence; every used implication and all matching pins were
checked. Only written mathematics and text/hash operations were used.
Frozen and public files were not edited.
