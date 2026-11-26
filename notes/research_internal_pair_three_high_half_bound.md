# The second half of the mixed power-three Fourier period

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

This note bounds the original mixed source on half of its full
Fourier period. The remaining outer Newton index is kept in its
finite sum. Only the complete-meridian trace is deformed. An
elementary maximum principle in the fixed wire coordinate reduces
the required phase bounds to six two-dimensional contour faces.

Use the exact source and geometric root of
[the local mixed-packet theorem](research_internal_pair_three_mixed_packet.md):
\[
 W_{3,N}(x)=\phi_N[R^3\mathbf B_N(x)K_N(\,\cdot\,,-2)],
 \qquad
 Y=\Im x_*>0,\qquad M=\Re S(x_*,0).
 \tag{1}
\]
The root, its branches, and its original logarithmic normalization
are those fixed in that theorem. In particular its enclosure gives
\[
 M>\frac54+\frac1{100},\qquad
                  2\pi Y>\frac7{20}.
 \tag{2}
\]

**Theorem 1.** There are constants \(C,A\), independent of the
integer level \(N\) and of \(a\in[1/2,1]\), such that
\[
                |W_{3,N}(a+iY)|\le CN^A e^{5N/4}.
 \tag{3}
\]
Thus the square of this source on that half-period has a strict
exponential gap below the geometric rate \(2M\).
The conclusion holds at both level parities.

## 1. Physical values and normals before deforming the trace

Write \(D=N-1\), and let
\(\tau_j=\pi-(2j+1)\pi/N\) represent a distinct physical
angle. The exact physical value of the continued Newton factor is
\[
 B_N(x,\tau_j)
 =\frac{\sin(\pi Nx)}{N\sin(\pi x)}
        \prod_{k=1}^j
          \frac{\sin\pi(x+k/N)}{\sin\pi(k/N-x)}.
 \tag{4}
\]
At a double root, its angular derivative is
\[
 \partial_tB_N(x,\tau_j)
 =-\frac12 B_N(x,\tau_j)
                  \sum_{k=j+1}^{D-j}\cot\pi(k/N-x).
 \tag{5}
\]
These are the full value-and-normal identities in
[the finite Fourier-band proof](research_newton_interpolation_finite_fourier_band.md),
Lemma 1. No distinct-root quotient replaces the physical algebra.

For \(x=a+iY\), \(1/2\le a\le1\), and \(1\le k\le j<N/2\),
\[
 |\sin\pi(x+k/N)|^2-|\sin\pi(k/N-x)|^2
              =\sin(2\pi a)\sin(2\pi k/N)\le0.
 \tag{6}
\]
Every ratio in (4) therefore has modulus at most one. Since
\(|\sin(\pi x)|\ge\sinh(\pi Y)\), equations (4)--(5) give
\[
 |B_N(x,\tau_j)|\le C N^{-1}e^{\pi NY},\qquad
 |\partial_tB_N(x,\tau_j)|\le C e^{\pi NY}.
 \tag{7}
\]
For the second estimate use
\(|\cot\pi(k/N-x)|\le\coth(\pi Y)\).
An ordinary spectral normal is
\((2\sin\tau_j)^{-1}\partial_t\). At every double root its
extra factor is polynomial in \(N\). At the odd simple root
\(\tau=0\), only the value is used. Thus the entire original
Hermite norm has upper rate \(\pi Y\), uniformly on this
half-period.

Set
\[
 \alpha=\frac1{32},\quad \beta=\frac{15}{32},\quad
 T=\frac{39}{20},\quad H=\frac7{20},\qquad
                    g(y)=J(2y)-4J(y).
 \tag{8}
\]
Remove outer Newton indices with \(j/N\notin[\alpha,\beta]\)
before the trace. The original Hermite bounds used in Section 4
of the local mixed-packet proof give rate at most \(2g(\alpha)\)
for their two outer Newton factors. The fixed crossing values
and first normals cost only powers of \(N\). By (7), this whole
discarded sum has upper rate
\[
                         \pi Y+2g(\alpha)<\frac54.
 \tag{9}
\]
Next remove physical trace nodes with \(|t|\ge T_N\), where
\(T_N\ge T\) is an original midpoint and
\(T_N-T=O(N^{-1})\).
The [real outer-angle bound](research_terminal_real_angle_tail.md)
applies because \(\pi/2<T<2\pi/3\).
It controls every retained outer-wire subset, including its
first normal, by a polynomial times \(e^{N\psi(T,0)}\).
Equation (7) then gives upper rate
\[
                          \pi Y+\psi(T,0)<\frac54.
 \tag{10}
\]
Both strict comparisons are included in the outward certificate
below. Their enclosed upper bounds are less than \(701/1000\)
and \(1121/1000\), respectively; these rounded inequalities only
describe the stronger bounds saved in the record.

## 2. Factorial branches on the trace rectangle

On the retained source use
\[
 B_N(x,t)=
 \frac{N}{
  G_N(N(1/2-x+t/(2\pi))-1/2)
  G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{11}
\]
For \(x=a+iY\), \(a\in[1/2,1]\), and
\(|\Im t|\le H<2\pi Y\), both shifted arguments in (11)
have imaginary parts strictly below zero. The argument \(x\)
is strictly above the real axis. Their real parts may cross
zero or one, but none of these factors meets a zero or pole.

Here is a direct uniform asymptotic justification across those
real-part boundaries. The
[exact factorial formula](research_exact_cyclotomic_factorial.md)
gives, on the lower half-plane,
\[
 \log G_N(Nz)
  =\frac12\log N-\frac{i\pi N}{12}
                  +\sum_{k=0}^{N-1}L(z-k/N).
 \tag{12}
\]
The displayed function \(L\) in that formula is holomorphic
on the entire lower half-plane. Euler--Maclaurin on a compact
subset of it gives
\[
 \log G_N(Nz)
   =NJ_-(z)+\frac12\log N+\frac12J_-'(z)+O(N^{-1}),
 \quad
 J_-(z)=\int_0^1L(z-v)\,dv-\frac{i\pi}{12}.
 \tag{13}
\]
Indeed \(J_-'(z)=L(z)-L(z-1)\), so the first endpoint
correction in the sum is \(J_-'/2\). On the overlap with
\(0<\Re z<1\), comparison with the established factorial
expansion identifies \(J_-\) with the original sine primitive.
This fixes its additive constant and branch. Euler--Maclaurin
also gives all fixed derivative bounds and bounded offsets;
the upper half-plane statement follows by conjugation.

For a real outer index \(y=j/N\in[\alpha,\beta]\), its shifted
arguments can meet the negative real axis at zero trace height.
The [uniform reciprocal-factorial bound](research_uniform_factorial_and_boundary_decay.md),
equation (4), applies there and includes every reciprocal zero.
Consequently the retained summand has a uniform polynomial
upper bound with phase
\[
 \begin{split}
 F_x(y,t)
   &=b(x,t)+b(y,t)+b(y,0)+\frac{3it^2}{4\pi}-it,\\
 b(x,t)
   &=-J_-(1/2-x+t/(2\pi))
     -J_-(1/2-x-t/(2\pi))-2J_+(x).
 \end{split}
 \tag{14}
\]
For \(b(y,t)\), the argument \(1/2-y+t/(2\pi)\) uses
the lower continuation on \(t=\tau-ih\), and the other
shifted argument uses the upper continuation. These are the
same branches as in the original trace-first proof. Their real
boundary values agree where \(h=0\).

## 3. The maximum over the high half occurs at an endpoint

**Lemma 2.** Fix \(Y>H/(2\pi)\). For
\(|\tau|\le49/25\), \(0\le h\le H\), and \(t=\tau-ih\),
\[
 \max_{1/2\le a\le1}\Re b(a+iY,t)
     =\max\{\Re b(1/2+iY,t),\Re b(1+iY,t)\}.
 \tag{15}
\]

*Proof.* All shifted factorial arguments stay off the real axis,
so differentiation along \(a\) is legitimate. Put
\(c=\cos(2\pi(a+iY))\), \(d=\cos t\). Then
\[
 \partial_a\Re b(a+iY,t)
     =\log\left|\frac{c+d}{1-c}\right|.
 \tag{16}
\]
The sign of this derivative is the sign of
\[
 D(a)=|d|^2-1+2\Re\{c(1+\overline d)\}.
 \tag{17}
\]
The numerator in (16) is a product of the two nonzero
shifted sine factors in (14), and its denominator is also
nonzero. The function \(D\)
is a constant plus one sinusoid in \(2\pi a\). Its endpoint
values are
\[
 D(1/2)=C-2A,\qquad D(1)=C+2A,
 \quad
 C=\sinh^2h-\sin^2\tau,\quad
 A=\cosh(2\pi Y)(1+\cos\tau\cosh h).
 \tag{18}
\]
The elementary inequalities
\[
 \cos(49/25)>-\frac25,\qquad
 \cosh(7/20)<\frac87
 \tag{19}
\]
imply \(|C|\le1\) and \(2A>2(1-\frac25\frac87)>1\).
For the first bound in (19), substitute \(49/25\) into
the lower Taylor polynomial \(1-z^2/2+z^4/24-z^6/720\).
For the second, use
\(\cosh h\le(1-h^2/2)^{-1}\).
Thus \(D(1/2)<0<D(1)\).

A nonconstant sinusoid plus a constant has at most two zeros
in a full period. Opposite endpoint signs on this half-period
therefore give exactly one zero, with a change from negative
to positive. The function in (15) decreases and then increases.
Its maximum is at an endpoint. \(\square\)

The other terms in \(F_x\) are independent of \(a\), so (15)
applies to the whole phase (14). It applies to the lower trace
line and both folded vertical sides.

## 4. Six outward phase bounds

Keep the outer wire \(y\) real. For each
\(a\in\{1/2,1\}\), the certificate verifies
\[
 \begin{array}{ll}
 \Re F_{a+iY}(y,\tau-iH)<5/4,
   &\alpha\le y\le\beta,\quad
       |\tau|/(2\pi)\le311/1000,\\[1mm]
 \Re F_{a+iY}(y,T-ih)<5/4,
   &\alpha\le y\le\beta,\quad0\le h\le H,\\[1mm]
 \Re F_{a+iY}(y,-T-ih)<5/4,
   &\alpha\le y\le\beta,\quad0\le h\le H.
 \end{array}
 \tag{20}
\]
The enlarged lower interval contains \([-T_N,T_N]\) for all
sufficiently large \(N\), since
\[
 T<2\pi(311/1000)<49/25.
 \tag{21}
\]
Each of the six compact surfaces has a finite rational-box
cover, with strict outward upper bounds. Hence a sufficiently
small change from \(T\) to \(T_N\) on the vertical sides
preserves a strict bound below \(5/4\). This uses uniform
continuity of the continued real primitive, including at its
integrable moving-zero points.

Run the certificate with

~~~sh
python3 experiments/certify_internal_pair_three_high_half.py
~~~

The [script](../experiments/certify_internal_pair_three_high_half.py)
retains the algebraic root enclosure from the local-packet proof,
the lower/upper factorial branches, and the actual filling
terms. Every comparison uses outward Arb/Acb arithmetic.
The [saved record](../repro/results/research-internal-pair-three-high-half.json)
contains all six covering proofs, the two tail bounds (9)--(10),
and the source hashes. It certifies these inequalities; the
exact finite-source passage is the next argument.

## 5. The exact trace proves the claimed source bound

After the two original removals in Section 1, the trace
representative is
\[
 f_N(t)=B_N(x,t)
           \sum_{j/N\in[\alpha,\beta]}
                     B_N(j/N,t)B_N(j/N,0).
 \tag{22}
\]
It is even and holomorphic on the whole trace rectangle.
The fixed-wire factor has the same physical values and first
normals as \(\mathbf B_N(x)\), and the other factors are the
literal original Newton polynomials at each retained integer.
Thus (22) represents the exact retained finite source.

Apply Corollary 3 of
[the complete-trace contour identity](research_exact_complete_trace_contour.md)
at the midpoint cutoffs \(\pm T_N\), with height \(H\).
On the lower side its full double-pole kernel is
\[
       \frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \tag{23}
\]
Its denominator is bounded away from zero, uniformly for
large \(N\). The numerator is exactly the charge term in
(14). There is no need to separate its higher charges.
Equations (14)--(15) and the first line of (20) bound
each retained wire term by a polynomial times \(e^{5N/4}\).
There are at most \(N\) such terms.

The exact vertical contribution has kernel
\(1/(4\cosh^2(Nh/2))\). After using the oddness of
\(\sin t\,f_N(t)e^{3iNt^2/(4\pi)}\), its two halves
are bounded on \(t=T_N-ih\) and \(t=-T_N-ih\),
\(0\le h\le H\). Since
\[
                  (4\cosh^2(Nh/2))^{-1}\le e^{-Nh},
 \tag{24}
\]
its exponent is again bounded by (14). The last two lines
of (20), with (15), control the complete vertical contribution,
including its zero-height end. No \(1/h\) estimate is introduced.

The trace prefactors, sine amplitude, contour lengths, and the
remaining number of wire terms contribute only powers of \(N\).
Adding back the two strict original errors (9)--(10) proves
(3). Enlarging \(C\) covers the finitely many smaller levels.
\(\square\)

This establishes the high half of the full circle only. It does
not yet estimate the part \(0\le\Re x<1/2\) outside the local
geometric window. The exact circle representation still requires
that remaining comparison before its local packet gives the
complete internal-pair asymptotic.
