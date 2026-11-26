# A square formula for the symbol of every odd inner crossing

Private research proof, 8 November 2026. The positive Fourier symbol
found for the inner crossing power three is one member of an exact
family. Every fixed signed odd inner power has symbol at least four
on the entire real character circle. Consequently its actual weighted
adjoint has a bounded Dirichlet inverse on each fixed interior color
interval. The outer crossing power may be any fixed integer.

This is an interior statement. It does not estimate the complete-color
boundary terms or establish a volume limit for a new family of knots.
The argument is algebraic and uses no numerical evaluation.

## 1. The original operator for a general inner power

Retain the full algebra and normalization of the
[seven-term source theorem](research_mixed_next_physical_inner_seven_term_recurrence.md).
Thus
\[
 q=e^{\pi i/N},\quad D=N-1,\quad \eta=(-1)^D,
 \quad\kappa=q^{D^2/2},\quad
 \mathcal A_N=\mathbb C[z]/(P_N),\quad P_N=2T_N(z/2)+2,
\]
\[
 T^2=I,\qquad \mathcal L=TZT,\qquad
 \mathcal L_s=R^{-s}\mathcal L R^s,\qquad
 F_N=K_N^{\rm ord}(-2,\cdot).
\]
Here \(Z\) denotes multiplication by \(z\), and \(R\) is the
original crossing multiplication operator, with its full Hermite jets.
For any integer \(n\), define
\[
 Q_{n,N}=TR^nF_N,\qquad
 \mathcal B_{n,N}=T\mathcal L_{-n}T,
 \qquad \mathcal D_{n,N}=\mathcal B_{n,N}+2I.                 \tag{1}
\]
The original kernel identity gives
\[
 (\mathcal L+2)F_N=-\eta P_N(-2)e_D/N^2.
\]
Conjugation by \(TR^n\), together with \(R^ne_D=\kappa^ne_D\)
and \(Te_D=1\), proves the exact full-algebra equation
\[
 \mathcal D_{n,N}Q_{n,N}=\mathfrak f_{n,N}1,
 \qquad
 \mathfrak f_{n,N}=
 \begin{cases}4\kappa^n/N^2,&N\text{ even},\\0,&N\text{ odd}.
 \end{cases}                                                   \tag{2}
\]
This calculation is valid for negative powers as well.

The exact crossing recurrence and turn identities in
[current-free transport, equations (24),(28)](research_current_free_aw_crossing_transport.md)
imply
\[
 \mathcal B_{0,N}=Z,\quad \mathcal B_{1,N}=\mathcal L_1,
 \quad \mathcal B_{-1,N}=\mathcal L_{-1},
\]
\[
 \mathcal B_{n+1,N}+q^{-1}\mathcal L\mathcal B_{n,N}
       +q^{-2}\mathcal B_{n-1,N}=8q^{-1}I.                     \tag{3}
\]
The order of multiplication in (3) is part of the identity. Each
\(\mathcal D_{n,N}\) has physical shift width at most \(|n|\)
for \(n\ne0\): this follows inductively from (3) in either direction,
starting with \(Z\) and the three-term operators \(\mathcal L_{\pm1}\).
Equation (2), evaluated away from the endpoint collars of that width,
is therefore a finite recurrence for the actual physical values of
\(Q_{n,N}\).

## 2. The scalar recurrence for the leading symbol

Let \(0<u<\pi\), write \(\zeta=e^{iv}\), and put
\[
 a=\cot^2(u/2),\qquad
 \ell=2+2a-a(\zeta+\zeta^{-1}),\qquad
 m=2+2a-a(e^{-iu}\zeta+e^{iu}\zeta^{-1}).                    \tag{4}
\]
These are the original leading symbols of \(\mathcal L\) and
\(\mathcal L_1\), respectively. The physical multiplication symbol
is \(-2\cos u\). Passing to the leading coefficients in (3) therefore
gives a unique two-sided scalar sequence
\[
 B_0=-2\cos u,\qquad B_1=m,\qquad
 B_{n+1}+\ell B_n+B_{n-1}=8.                                  \tag{5}
\]
The leading symbol of \(\mathcal D_{n,N}\) is \(d_n=B_n+2\).
For \(n=3\), (5) gives precisely
\[
 d_3=(\ell^2-1)m-(8+2\cos u)\ell+10,
\]
the symbol used in the earlier all-character theorem.

Define real numbers
\[
 C=\cos(u/2)>0,\qquad k=\cot(u/2)\sin(v/2),\qquad
 h=\cos(v/2).
\]
The angle-addition formula yields
\[
 \ell=2+4k^2,\qquad m=2+4C^2(k-h)^2,
 \qquad B_0=2-4C^2,\qquad k^2+1-h^2=k^2/C^2.                \tag{6}
\]
Let the real sequence \(w_n\), for all integer indices, be defined by
\[
 w_0=1,\qquad w_1=k-h,\qquad w_{n+1}=2kw_n+w_{n-1}.           \tag{7}
\]
Negative indices are specified uniquely by the same recurrence.

**Theorem 1.** For every integer \(n\),
\[
 \boxed{\quad B_n=2+4C^2(-1)^{n+1}w_n^2,\qquad
 d_n=4+4C^2(-1)^{n+1}w_n^2.\quad}                            \tag{8}
\]
In particular, for every signed odd integer \(n\),
\[
                  d_n(u,\zeta)\ge4
                  \qquad(0<u<\pi,\ |\zeta|=1).              \tag{9}
\]

*Proof.* The determinant expression
\(\Delta_n=w_{n+1}w_{n-1}-w_n^2\) changes sign at each step
of (7). At \(n=1\), equations (6),(7) give
\[
 \Delta_1=2k(k-h)+1-(k-h)^2=k^2+1-h^2=k^2/C^2.
\]
Thus, for all integer \(n\),
\[
 \Delta_n=(-1)^{n-1}k^2/C^2,\qquad
 w_{n+1}^2-(2+4k^2)w_n^2+w_{n-1}^2=2\Delta_n.              \tag{10}
\]
The second identity follows by squaring
\(w_{n+1}-w_{n-1}=2kw_n\).
Substitute the proposed expression (8) into the left side of (5).
Its constant part is \(2(\ell+2)=8+8k^2\); its remaining part,
by (10), is \(-8k^2\). It therefore satisfies (5). Equations
(6),(7) give the required values at indices zero and one. Uniqueness
of the two-sided recurrence proves (8). Odd \(n\) then gives (9).
Although \(k,h\) change sign when \(v\) is increased by \(2\pi\),
\(w_n\) changes by \((-1)^n\). Hence (8) is well defined on
the character circle. \(\square\)

For example \(w_3=(4k^2+1)(k-h)+2k\), so the earlier
three-crossing inequality has the exact square representation
\(d_3=4+4C^2[(4k^2+1)(k-h)+2k]^2\).

The odd restriction matters. For \(n=2\), the same formula reads
\(d_2=4-4C^2[2k(k-h)+1]^2\). At \(u=\pi/2\), it is positive
at \(v=0\) and negative at \(v=\pi\). Continuity gives a real
character at which it vanishes. Thus the present positive-symbol
argument does not extend to every even inner power.

## 3. The actual adjoint for any fixed outer power

Write \(U=\lfloor N/2\rfloor-1\),
\(c_j=2\cos((2j+1)\pi/N)=-2\cos u_j\), and
\(u_j=\pi-(2j+1)\pi/N\). The original consumed-normal weights are
\(\beta_{j,N}=(-1)^{U+j}\omega_N(u_j)\), where
\[
 \omega_N(u)=
 \begin{cases}\sin u,&N\text{ even},\\
 \sin u\sin(u/2)/\cos^2(\pi/(2N)),&N\text{ odd}.
 \end{cases}
\]
These are equations (16)--(18) of the seven-term source theorem.
For an arbitrary fixed integer outer power \(p\), keep
\[
 \mu_{j,N}^{(p)}=\beta_{j,N}R(c_j)^p
   =(-1)^{U+(p+1)j}\kappa^p\omega_N(u_j)q^{pj(j+1)}.          \tag{11}
\]
The exact ratio, for a shift \(r\), is
\[
 \frac{\mu_{i-r,N}^{(p)}}{\mu_{i,N}^{(p)}}
 =(-1)^r e^{ipru_i+\pi i p r^2/N}
          \frac{\omega_N(u_i+2\pi r/N)}{\omega_N(u_i)}.       \tag{12}
\]
Indeed the power of \(q\) contributes
\(e^{-\pi ipr}e^{ipru_i+\pi ipr^2/N}\); combining its first
factor with \((-1)^{(p+1)r}\) leaves \((-1)^r\).

Let \(s=|n|\), with \(n\) odd, and write the interior recurrence
as \((D_{n,N}f)_j=\sum_{r=-s}^s d_{j,r,N}f_{j+r}\).
Its original bilinear weighted adjoint is
\[
 (A_{n,p,N}h)_i=\sum_{r=-s}^s
       \frac{\mu_{i-r,N}^{(p)}}{\mu_{i,N}^{(p)}}
           d_{i-r,r,N}h_{i-r}.                                \tag{13}
\]
On every fixed compact interval inside \((0,\pi)\), its
coefficients and their leading angular derivatives are uniformly
bounded. Their difference from their leading coefficients is
\(O(N^{-1})\). This follows directly by finite composition in
(3) of the original analytic three-term coefficients, and (12).
All constants may depend on the fixed integers \(n,p\) and on
the compact interval. No estimate uniform in growing crossing powers
or shrinking endpoint collars is asserted.

For a Fourier sequence \(h_j=e^{ij\vartheta}\), the frozen
symbol of (13) is
\[
                     d_n(u,-e^{i(pu-\vartheta)})\ge4.         \tag{14}
\]
This includes the physical half-step in (12).

**Corollary 2.** Fix an odd integer \(n\), an integer \(p\),
and a compact interval \(J\Subset(0,\pi)\). For all sufficiently
large \(N\) and every consecutive interval \(I_N\) of physical
indices in \(J\), compress (13) by zero extension of its test
sequence. The resulting square matrix satisfies
\[
 \operatorname{Re}\langle f,A_{I_N,N}f\rangle\ge3\|f\|_2^2,
 \qquad \|A_{I_N,N}^{-1}\|_{2\to2}\le1/3.                   \tag{15}
\]
The inner product in (15) is the ordinary auxiliary Hermitian
inner product; it does not change the bilinear pairing in (13).

*Proof.* Apply the finite sliding-window proof of the
[interior inverse theorem](research_mixed_next_outer_interior_dirichlet_inverse.md)
with width \(s\) in place of three. With windows of length
\(L=\lfloor\sqrt N\rfloor>s\), their exact overlap is
\(1-|r|/L\). If the coefficient bounds are \(C_0,C_1,C_2\)
as in that theorem, the real part is bounded below by
\[
 \left[4-\frac{(2s+1)C_1}{N}
          -\frac{2\pi(2s+1)C_2L}{N}
          -\frac{s(s+1)C_0}{L}\right]\|f\|_2^2.              \tag{16}
\]
Here Fourier orthogonality uses (14), and
\(\sum_{r=-s}^s|r|=s(s+1)\). The losses tend to zero for
fixed \(n,p,J\). Cauchy--Schwarz then proves the inverse bound,
exactly as for the seven-term operator. \(\square\)

## 4. What the inverse leaves in the original sum

For arbitrary nodal data \(g_i\), solve \(A_{I_N,N}h=g\)
and extend \(h\) by zero outside \(I_N\). With
\(q_{j,N}=Q_{n,N}(c_j)\), exact reindexing and (2) give
\[
 \sum_{i\in I_N}\mu_{i,N}^{(p)}g_iq_{i,N}
 =\mathfrak f_{n,N}\sum_{j\in I_N}\mu_{j,N}^{(p)}h_j
  -\sum_{r=-s}^s\sum_{\substack{j\in I_N\\j+r\notin I_N}}
            \mu_{j,N}^{(p)}h_jd_{j,r,N}q_{j+r,N}.              \tag{17}
\]
There are at most \(s(s+1)\) pairs in the last sum. Every
outside source value remains the original value; the zero extension
was imposed only on the test. Since \(|\mu_{j,N}^{(p)}|\le2\),
the even forcing is at most \(8\|g\|_\infty/(3N)\), and the
odd forcing is zero. No approximation residual appears.

The boundary values in (17), and their coefficients, have not been
estimated at the volume rate. The full Hermite endpoint conditions
also remain part of (2). The result extends the interior method to
all fixed signed odd inner powers; it does not establish stability
under arbitrary short partial fillings.

## Sources retained

- Full seven-term algebra, complete-end input, and consumed-normal weights:
  `49cd08c5759bd6669d3cbf1a7e661d60188639c9added0c973659c4723d0a21a`.
- Exact crossing recurrence and turn identities:
  `f81b9fc3edc2504c5250ad283bf0ceff191a1fc3a310c00fdb57602362f0bf4a`.
- Earlier all-character symbol and coefficient conventions:
  `c88ba98093fc147f5acfcf1790aa5b6f0f26edda6d741d2efc7c55315942e55e`.
- Finite sliding-window inverse proof:
  `e1b713461bacdf263c07c3baa21de67960fae5e5e2735e5c400c009c987afddf`.
