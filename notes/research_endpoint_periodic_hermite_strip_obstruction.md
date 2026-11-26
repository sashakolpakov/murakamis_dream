# A full-period strip bound forced by the endpoint kernel's normals

Private written proof, 16 November 2026.

Polynomial bounds on physical endpoint values and normals do not give
a moderate global periodic representative. For the microscopic endpoint
kernel, no even periodic holomorphic representative of its full data
can have polynomial norm on a strip of fixed positive height.
The obstruction is an explicit top Fourier coefficient of the actual
kernel. It applies to all such representatives, not only to the
canonical polynomial. It does not imply exponential growth of the
original closing scalar.

## 1. The original endpoint data

Put
\[
 N\ge2,\quad D=N-1,\quad \eta=(-1)^D,\quad \theta=\pi/N,
 \qquad c_a=2\cos((2a+1)\theta),
\]
\[
 S_j=\prod_{r=1}^j2\sin(r\theta),\quad S_0=1,\qquad
 e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z),\qquad
 K_N(w,z)=\sum_{j=0}^D e_j(w)e_j(z).
 \tag{1}
\]
The physical relation and top Newton polynomial satisfy
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 (z-c_0)e_D(z)=\frac{\eta}{N^2}P_N(z).
 \tag{2}
\]
The latter is the exact original identity, with \(S_D=N\).
For real \(\alpha\) define
\[
 w_N(\alpha)=2\cosh(\alpha/N),\qquad
 B_{N,\alpha}(t)=K_N(w_N(\alpha),-2\cos t).
 \tag{3}
\]
This is an even Laurent polynomial with frequencies \(|k|\le D\).
Write its Fourier coefficients as \(b_k\), using \(e^{ikt}\).
Only its top Newton summand contributes to \(b_D\).
Since \([z^D]e_D=\eta/N^2\) and
\((-2\cos t)^D\) has top Fourier coefficient \((-1)^D=\eta\),
\[
 \boxed{\quad
 b_D=\frac{e_D(w_N(\alpha))}{N^2}
 =\frac{4\eta\cosh^2(\alpha/2)}
 {N^4\{2\cosh(\alpha/N)-2\cos(\pi/N)\}} .
 \quad}
 \tag{4}
\]
There is no vanishing denominator for real \(\alpha\).
For every fixed \(A<\infty\), uniformly on \(|\alpha|\le A\),
\[
 b_D=\frac{\eta}{N^2}
       \frac{4\cosh^2(\alpha/2)}{\alpha^2+\pi^2}
                  (1+O_A(N^{-2})).
 \tag{5}
\]
An all-level lower bound is also useful. The elementary estimates
\(\cosh u-1\le u^2\cosh u/2\) and \(1-\cos u\le u^2/2\)
give
\[
 N^2(w_N(\alpha)-c_0)\le
 C_A:=A^2\cosh(A/2)+\pi^2,\qquad
                         |b_D|\ge\frac4{C_A N^2}.
 \tag{6}
\]

## 2. A Fourier functional determined by the full physical jets

The full angular grid is
\[
 \tau_j=\frac{\pi(D-2j)}N,\quad 0\le j<N,\qquad
                         e^{iN\tau_j}=\eta.
 \tag{7}
\]
Fix \(H>0\). Let \(h\) be even and \(2\pi\)-periodic, holomorphic
on \(|\Im t|<H\), continuous on its closed strip, and put
\[
 M_H(h)=\sup_{\substack{-\pi\le\Re t\le\pi\\|\Im t|\le H}}|h(t)|.
 \tag{8}
\]
Suppose \(h\) has the original full physical data of \(B_{N,\alpha}\).
Equivalently,
\[
 h(\tau_j)=B_{N,\alpha}(\tau_j),\qquad
 h'(\tau_j)=B_{N,\alpha}'(\tau_j)\quad(0\le j<N).
 \tag{9}
\]
At a double spectral node the angular derivative is its spectral
normal times \(2\sin\tau_j\). The negative preimages are supplied by
evenness. At odd levels the simple spectral node \(-2\) has preimage
zero: only its value is prescribed, and both angular derivatives
there vanish by evenness. Thus (9) imposes no additional odd normal.
It also covers \(N=2\), whose two angles represent its single
double node.

For an even periodic holomorphic \(h(t)=\sum_{k\in\mathbb Z}a_ke^{ikt}\),
define the original-grid functional
\[
 \Lambda_N(h)=\frac1{N^2}\sum_{j=0}^{N-1}
        \{h(\tau_j)+h'(\tau_j)/i\}\,e^{i\tau_j}.
 \tag{10}
\]
The finite exponential sum in (7) gives exactly
\[
 \Lambda_N(h)=\sum_{m\in\mathbb Z}
                         m\eta^m a_{mN-1}.
 \tag{11}
\]
Indeed the average of \(e^{i(k+1)\tau_j}\) is zero unless
\(k+1=mN\); when it is nonzero, it equals \(\eta^m\).
The derivative supplies \(k+1\), and the remaining normalization
in (10) supplies \(1/N\).
For \(B_{N,\alpha}\), its band \(|k|<N\) leaves only \(k=-1,D\);
the first has coefficient \(k+1=0\). Hence
\[
             \Lambda_N(h)=\Lambda_N(B_{N,\alpha})=\eta b_D.
 \tag{12}
\]
This is the top-coefficient case of the archived full-Hermite
folding formula. The disappearance of the low-frequency alias
uses the normals, not just the values.

## 3. The quantitative obstruction and its scope

**Theorem.** Every \(h\) satisfying (8)--(9) obeys
\[
 \boxed{\quad
 M_H(h)\ge |b_D|\,
       \frac{(1-e^{-NH})^2}{2\cosh H}\,e^{NH}
 \ge \frac{2(1-e^{-2H})^2}{C_A\cosh H}\,
                         N^{-2}e^{NH}
 \quad}
 \tag{13}
\]
when \(\alpha\) is real and \(|\alpha|\le A\).
In particular no family with these full data has polynomial, or
subexponential, norm on a fixed strip of positive height.

*Proof.* Moving the Fourier coefficient integral to either horizontal
line of height less than \(H\), then taking the height to \(H\),
gives
\[
                         |a_k|\le M_H(h)e^{-H|k|}.
 \tag{14}
\]
Periodicity cancels the vertical integrals. The closed-strip
continuity justifies the limiting bound. These estimates imply
absolute convergence of both the value and derivative Fourier series
on the real axis, so every interchange in (10)--(11) is valid.
Equations (11)--(12) now give
\[
 \begin{split}
 |b_D|
 &\le M_H(h)\sum_{m\ne0}|m|e^{-H|mN-1|}\\
 &=M_H(h)(e^H+e^{-H})\sum_{m\ge1}m e^{-mNH}\\
 &=M_H(h)\frac{2\cosh H\,e^{-NH}}{(1-e^{-NH})^2}.
 \end{split}
 \tag{15}
\]
Rearrange and use (6) and \(N\ge2\) to prove (13).
No parity subsequence has been selected. \(\square\)

The theorem includes the canonical polynomial \(B_{N,\alpha}\).
It also includes any single-valued holomorphic spectral
representative whose pullback by \(z=-2\cos t\) is defined on this
entire strip and has the full physical jets. Adding a holomorphic
multiple of \(P_N\) does not evade (13) when the resulting
representative still has these global periodic-strip properties.

The periodic hypothesis is essential to the argument. A local
interpolant or an even nonperiodic representative on a cut rectangle
need not satisfy (14), because its Fourier contour has boundary
terms. Those terms must be retained in an exact source substitution.
The theorem makes no assertion about interpolation in the physical row
degree, particularly after a radical has already consumed the normal
and only row values remain.

There is also no conclusion about the growth of a closing scalar.
For example, the original trace has normalization
\(\phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f\), so (1) gives
the exact identity
\[
 \phi_N^{(z)}K_N(w_N(\alpha),z)=e_D(w_N(\alpha)).
 \tag{16}
\]
This is bounded uniformly for real \(|\alpha|\le A\): its numerator
in (2) is at most \(4\cosh^2(A/2)\), while
\(N^2(w_N(\alpha)-c_0)\ge4\).
Thus the kernel's own original trace is bounded even though every
global periodic full-Hermite strip representative satisfies (13).
Arbitrary shared spectators and the actual filled-source closing
remain separate from this norm statement.

## 4. Coverage and pinned sources

The Fourier folding identity itself is already proved in the first
source below. The additional conclusion is its application to the
explicit top coefficient (4) of the full microscopic endpoint kernel,
uniformly at both parities. The original off-grid difference equation
also forces large canonical-kernel values, but no additional
three-shift argument is needed here.

The entire following direct sources were read at these versions, and
their used implications and hashes checked:

* [Boundary crossing packet preservation](research_boundary_crossing_packet_preservation.md),
  SHA256 a2f9cadf0fd6f23889ea7d20b469055fe33cb9df4d971668a2923666983cfec8:
  Section 2, the exact full-Hermite Fourier folding and the odd
  zero-angle convention.
* [Original edge difference equation](research_edge_kernel_difference_and_endpoint_bound.md),
  SHA256 5d0d07d4d97d82cca66e0e0c3bf2cecad8e5f58ef8329178278b297cf0d6c5da:
  the actual Newton normalization, \(S_D=N\), and identity (2).
* [Full-period endpoint kernel reduction](research_full_period_endpoint_kernel_reduction.md),
  SHA256 a1d67ac803c0160bbfdacaa96a6fde9dc1ffae06fc39eb94f0416dcf2ecef76e:
  the original full-normal trace, both-parity endpoint data, and
  the distinction between polynomial physical bounds and a source rate.

Only written mathematics, source-text reads, and hashes were used.
No mathematical program, numerical experiment, test, or compilation
was run. Adopted notes and public manuscripts were unchanged.
