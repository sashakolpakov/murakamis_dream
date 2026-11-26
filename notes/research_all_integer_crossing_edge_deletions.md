# Shortening both edges beside an arbitrary integer crossing

Private research deduction, 9 November 2026. The error from deleting
the upper Newton rows of the two edges beside a traced vertex has a
bound independent of the integer crossing power. The incoming color
may be any point of the full real color interval. In particular, this
part of the source estimate does not require a large crossing power.

The argument keeps the original trace, including its derivatives at
double roots and its extra simple root at odd levels. It does not
estimate the trace with both edges shortened, whose signed
cancellation remains a separate problem. All arguments below are
written finite identities and analytic inequalities; no numerical
evaluation is used.

## 1. The source and the two deletions

Let \(N\ge3\), \(D=N-1\), \(m=\lfloor N/2\rfloor\), and \(U=m-1\).
Use the original algebra and trace
\[
 \mathcal A_N=\mathbb C[x]/(2T_N(x/2)+2),\qquad
 \phi_N(f)=(-1)^D N^2[x^D]\operatorname{rem}_{2T_N(x/2)+2}f .
 \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind. Put
\[
 c_a=2\cos((2a+1)\pi/N),\qquad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 e_j(x)=S_j^{-2}\prod_{a<j}(c_a-x),
 \tag{2}
\]
with empty products equal to one. The full and shortened edges are
\[
 \mathcal K_N(w,x)=\sum_{j=0}^{D}e_j(w)e_j(x),\qquad
 \mathcal K_N^<(w,x)=\sum_{j=0}^{U}e_j(w)e_j(x).
 \tag{3}
\]
The crossing \(R_N\) is the original invertible element of
\(\mathcal A_N\). Its values at every distinct physical root have
modulus one. Thus every signed integer power \(R_N^n\) is defined.

For \(z_u=-2\cos u\), define three exact finite functions:
\[
 \begin{split}
 Q_{n,N}(w,u)
   &=\phi_N[R_N^n\mathcal K_N(w,x)\mathcal K_N(x,z_u)],\\
 Q_{n,N}^{<}(w,u)
   &=\phi_N[R_N^n\mathcal K_N(w,x)\mathcal K_N^<(x,z_u)],\\
 Q_{n,N}^{<<}(w,u)
   &=\phi_N[R_N^n\mathcal K_N^<(w,x)\mathcal K_N^<(x,z_u)].
 \end{split}
 \tag{4}
\]
Both superscripts refer to edge deletions; the trace in all three
lines remains the full trace (1). Write
\(\Delta^{\rm out}=Q-Q^<\) and
\(\Delta^{\rm in}=Q^<-Q^{<<}\).

We use the original complete-edge action
\[
 \psi(u,0)=\Psi_{1/2}(-2\cos u),\qquad
 \Psi_a(w)=\int_0^a
 2\operatorname{arsinh}\left(\frac{\sqrt{2-w}}2\cot(\pi s)\right)ds .
 \tag{5}
\]
The square root and inverse hyperbolic sine are principal on
\(\mathbb C\setminus[2,\infty)\). Its normalization is
\(\psi(0,0)=2b_2\), where \(b_2<7/12\) is the original real
Newton constant. These are the profiles and normalization of the
[physical-row slit theorem](research_mixed_next_first_short_edge_slit_plane_bound.md).

## 2. Bounds independent of the crossing power

**Theorem.** Fix \(K_0<\infty\). Constants \(C,A\), independent of
\(n\in\mathbb Z\), \(w\in[-2,2]\), and \(N\), can be chosen such that
\[
 |\Delta^{\rm out}_{n,N}(w,u)|
 \le CN^A e^{N\mathscr E(K)},\qquad
 \mathscr E(K)=\frac K2+\psi(iK,0)
       \le2b_2+\frac K2+\frac{K^2}{4\pi},
 \qquad K=|\Im u|\le K_0 .
 \tag{6}
\]
There is no restriction on \(\Re u\) in (6).
On \(|\Re u|\le\pi/2\), the other deletion satisfies
\[
 |\Delta^{\rm in}_{n,N}(w,u)|
 \le CN^A e^{N\Re\psi(u,0)}
 \le CN^A\exp N\left\{2b_2+\frac{K^2}{4\pi}\right\}.
 \tag{7}
\]
In fact \(\Re\psi(u,0)\le\psi(iK,0)\), as the horizontal
comparison below proves. Consequently
\[
 |Q_{n,N}(w,u)-Q_{n,N}^{<<}(w,u)|
 \le CN^A e^{N\mathscr E(K)}
 \tag{8}
\]
on that central strip. Every fixed ordinary derivative in \(w\)
obeys (6)--(8), with changed polynomial factors. These assertions
hold at both parities. They even allow an integer \(n=n(N)\);
no asymptotic assertion for the remaining trace is made in that
case.

### Physical rows throughout the real incoming interval

Put \(F_{a,N}(w)=\mathcal K_N(c_a,w)\).
The original Jacobi determinant formula gives
\[
 F_{a,N}(w)=
 \frac{\prod_{\nu=1}^{a}(\lambda_{a,\nu,N}-w)}
      {\prod_{j<a}A_{j,N}},\qquad
 A_{j,N}>0,\quad \lambda_{a,\nu,N}>c_0>0 ,
 \tag{9}
\]
for every physical ordinary row, including the last one; \(F_0=1\).
For real \(w\in[-2,2]\) and every \(\lambda>0\),
\(|\lambda-w|\le\lambda+2\). Hence
\[
              |F_{a,N}(w)|\le F_{a,N}(-2).
 \tag{10}
\]
It is not necessary to assume that the zeros in (9) exceed \(2\).

Equation (6) of the slit theorem is quantitative on compact
subsets of \(\Re w<2\). At \(w=-2\) it gives, uniformly in all
eligible indices,
\[
 F_{a,N}(-2)\le CN^A e^{N\Psi_{a/N}(-2)}.
 \tag{11}
\]
In particular the zero row and indices tending to \(N/2\) do not
require a separate limiting substitution.

### Outgoing deletion

The exact [radical contraction](research_high_newton_radical_contraction.md)
has coefficients \(b_{ra}\), with \(|b_{ra}|\le2\), and says
\[
 \phi_N(R_N^n e_{D-r}f)
   =\sum_{a=0}^r b_{ra}R_N(c_a)^n f(c_a),
       \qquad 0\le r<m .
 \tag{12}
\]
It holds for every integer \(n\). At a double root the factor
\(e_{D-r}\) vanishes, so the derivative in the original trace
falls on that factor. Derivatives of \(R_N^n\) and of \(f\)
do not occur in (12). This is why the estimate is uniform in
the crossing power.

Thus the radical part of \(\Delta^{\rm out}\) is exactly
\[
 \sum_{r=0}^{m-1}e_{D-r}(z_u)
     \sum_{a=0}^r b_{ra}R_N(c_a)^n F_{a,N}(w).
 \tag{13}
\]
The original Fourier coefficient bound for the radical basis,
with its actual degree retained, is
\[
 |e_{D-r}(z_u)|\le\sqrt{N-1}\,e^{(D-r)K}.
 \tag{14}
\]
Set \(v_r=\pi-2\pi r/N\). Since \(\Psi_a(-2)\) increases in \(a\),
the condition \(a\le r\) in (13) and (10)--(11) give
\[
 \begin{split}
 2b_2-\Psi_{r/N}(-2)
  &=\frac1\pi\int_0^{v_r}
             \operatorname{arsinh}(\tan(v/2))\,dv\\
  &\ge\frac{v_r^2}{4\pi}.
 \end{split}
 \tag{15}
\]
The inequality follows by differentiating the integrand:
its derivative is \(\tfrac12\sec(v/2)\ge\tfrac12\).
The integrable endpoint at \(v=\pi\) also covers \(r=0\).
First, combining (14)--(15) gives the simple quadratic ceiling
for the exponential rate of each term in (13):
\[
 2b_2+\frac K2+\frac{Kv_r}{2\pi}-\frac{v_r^2}{4\pi}
 =2b_2+\frac K2+\frac{K^2}{4\pi}
                       -\frac{(v_r-K)^2}{4\pi}.
 \tag{16}
\]
Here the exact degree gives an additional \(-K/N\), which
only decreases the bound.

We can retain the exact integral in (15) as well. Define
\[
 H(v)=\frac1\pi\int_0^v
                  \operatorname{arsinh}(\tan(s/2))\,ds ,
                  \qquad 0\le v\le\pi .
\]
Before its quadratic relaxation, the continuous rate maximum is
\[
 2b_2+\frac K2+
       \max_{0\le v\le\pi}\left\{\frac{Kv}{2\pi}-H(v)\right\}.
 \tag{16a}
\]
For \(K>0\), strict convexity of \(H\) gives one interior
maximizer, determined without a numerical optimization by
\[
 \operatorname{arsinh}(\tan(v_K/2))=K/2,\qquad
 v_K=2\arctan(\sinh(K/2))
     =2\arcsin(\tanh(K/2)).
 \tag{16b}
\]
At \(K=0\) the maximum is attained at \(v=0\). Denote the
maximum in braces by \(L(K)\). Differentiation at its unique
maximizer gives
\[
 L'(K)=\frac1\pi\arcsin(\tanh(K/2)),\qquad L(0)=0 .
 \tag{16c}
\]
The calibrated imaginary-axis formula (22) below therefore
identifies \(L(K)=\psi(iK,0)-2b_2\). Thus (16a) equals
\(\mathscr E(K)\) in (6). This is the exact maximum of this
absolute upper profile; no equality with the rate of the
signed error is inferred.

At odd \(N=2m+1\) the middle row is not radical. Its exact
additional contribution is
\[
 e_m(z_u)\left[
   \sum_{a=0}^{m-1}d_{ma}R_N(c_a)^n F_{a,N}(w)
                  +R_N(-2)^n\mathcal K_N(w,-2)\right],
 \quad
 d_{ma}=(-1)^{m+a}2\cos((m-a)\pi/N).
 \tag{17}
\]
This is the original identity for \(\phi_N(e_m f)\), applied
before taking absolute values. Its coefficients have modulus
at most two, and its simple-node scalar has modulus one.
The exact middle polynomial has degree \(m\) and norm at most
one on \([-2,2]\); therefore
\(|e_m(z_u)|\le2(m+1)e^{mK}\).
The all-real full-kernel bound gives
\(|\mathcal K_N(w,-2)|\le CN^A e^{2Nb_2}\).
Equations (10)--(11) bound the other rows in (17) at the same
rate. The odd contribution thus has rate at most
\(2b_2+K/2\le\mathscr E(K)\).
Polynomially many terms in (13),(17) prove (6).

### Incoming deletion with the other edge already shortened

The same exact contraction gives
\[
 \Delta^{\rm in,rad}_{n,N}(w,u)
 =\sum_{r=0}^{m-1}e_{D-r}(w)
       \sum_{a=0}^r b_{ra}R_N(c_a)^n F_{a,N}(z_u).
 \tag{18}
\]
Indeed \(\mathcal K_N^<(c_a,z_u)=F_{a,N}(z_u)\) for the double
rows \(0\le a<m\): all Newton terms of index greater than
\(a\) vanish there. For real \(w\), the first factor in
(18) is bounded by \(\sqrt{N-1}\).

The image \(z_u=-2\cos u\), for \(|\Re u|\le\pi/2\) and
\(|\Im u|\le K_0\), is a compact subset of \(\Re z<2\).
The quantitative estimate (6) of the slit theorem and the
monotonicity of \(\Re\Psi_a(z)\) give
\[
 |F_{a,N}(z_u)|\le CN^A e^{N\Re\psi(u,0)}
 \tag{19}
\]
uniformly over this set. At odd levels the additional expression
is
\[
 e_m(w)\left[
  \sum_{a=0}^{m-1}d_{ma}R_N(c_a)^n F_{a,N}(z_u)
                  +R_N(-2)^n\mathcal K_N^<(-2,z_u)\right].
 \tag{20}
\]
Here \(|e_m(w)|\le1\). The exact complete-end cardinal
interpolation in the slit theorem has polynomially bounded
absolute coefficient sum. Applying (19) to it also bounds
\(\mathcal K_N^<(-2,z_u)\) at rate \(\Re\psi(u,0)\).
This proves the first inequality in (7), with its original
odd simple-node term retained.

For completeness, its elementary scalar upper bound follows
directly from the original action derivative
\[
 \psi_u(u,0)=-\pi^{-1}\operatorname{arsinh}(\tan(u/2)).
 \tag{21}
\]
For \(0<\Re u\le\pi/2\), the tangent and its principal inverse
hyperbolic sine have positive real part. Thus the real part
of the action decreases along a horizontal line away from
the imaginary axis. Evenness and conjugation give the same
conclusion on the other half of the strip. On the axis,
\[
 \psi(-iK,0)
  =2b_2+\frac1\pi\int_0^K
                     \arcsin(\tanh(y/2))\,dy
  \le2b_2+\frac{K^2}{4\pi},
 \tag{22}
\]
since the derivative of \(\arcsin(\tanh(y/2))\) is
\(\tfrac12\operatorname{sech}(y/2)\le\tfrac12\).
Equations (21)--(22) prove the second inequality in (7).

Finally all differences are polynomials of degree at most \(D\)
in \(w\), regardless of \(n\). Markov's inequality on \([-2,2]\)
bounds every fixed ordinary derivative by a polynomial factor
times the displayed supremum. The complex-valued version follows
by rotating the derivative to the real axis and applying the
real polynomial inequality. This proves the derivative assertion
and completes the theorem.

## 3. Consequence for the symmetric three-block closing problem

At \(n=3\), \(w=-2\), the
[continued-action theorem](research_mixed_symmetric_closing_strip_phase_and_tail.md)
proves
\(\Re S_3(0,u)>321/200\) on
\[
       0\le\Re u\le\pi/2,\qquad -7/10\le\Im u\le0 .
\]
The error rate in (8) is less than \(623/400\) there.
Its gap below the continued action is greater than \(19/400\).
After absorbing the polynomial factor, (8) therefore gives
\[
 Q_{3,N}(-2,u)=Q_{3,N}^{<<}(-2,u)
                  +O\!\left(e^{N(\Re S_3(0,u)-1/25)}\right)
 \tag{23}
\]
uniformly on this rectangle, through both parities.

Thus shortening both edges costs less than the proposed geometric
contribution on this larger domain. Establishing that contribution
for the remaining full trace \(Q^{<<}\) still requires its central
finite-sum estimates and all contour remainders. Equation (23)
does not supply those estimates or locate the actual closing
stationary point inside the rectangle.

For other powers, the theorem supplies only the absolute error
bounds (6)--(8). A comparison with each power's own geometric
action is necessary before drawing the analogous conclusion.
Neither stability under arbitrary short partial fillings nor
the finite-exception volume theorem follows from these deletions
alone.

## Source versions

- Exact radical contraction for every signed integer power:
  1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03.
- Original odd middle-row contraction:
  b31ac2d1cbf5f0e3ab4b71b36af9718151bced51e6959ee32b26ccf7fac5dfe6.
- Full physical-row profiles, zeros, and cardinal interpolation:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Exact middle polynomial and full real incoming-color domains:
  9ffa400456a8439d55352156707fab0aacfb8f1f8b0f622fd66824c9f1e553db.
- Original outgoing deletion and all-real full-kernel bound:
  8b30fb2a8258d49fd8c162d5822c4652129ffc5a39ee77019e1b00aa2db7596e.
- Continued three-action and its larger-domain lower bound:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
