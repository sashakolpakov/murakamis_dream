# The full physical q-Hahn value and normal form a Gaussian–Hermite pair

Written proof, 24 November 2026.

The original ordinary column and its actual confluent partner have a
nondegenerate two-column Hermitian Gram after an explicit centering
and scaling. The ordinary column is Gaussian in its full physical
magnetic norm. Orthogonal projection removes the scalar part of the
normal and leaves its first Hermite mode. Both conclusions include
every physical magnetic coordinate, rather than a truncated window.

The result concerns one complete double channel at a real physical
degree separated from the two degree endpoints. It does not turn the
original bilinear gluing into a positive pairing. The proof
also computes the entrywise value-column Gram across a larger channel
window, retaining the original center phases.

## 1. Original columns, physical norm and the statement

Put \(q_0=e^{\pi i/N}\), \(d=N-1\), and take actual integers
\[
 0\le j<l,\qquad j+l=d,\qquad s=l-j,\qquad l\le t\le d.
 \tag{1}
\]
The physical magnetic indices are \(u=0,\ldots,t\). Write
\(\tau=t/N\), \(\xi=j/N\), and \(u_0=t/2\), which may be half-integral.
For \(q=q_0e^\epsilon\) use the marked logarithm
\(\log q=\pi i/N+\epsilon\), and set
\[
 Q=q^2,\quad B=Q^{-N},\quad x=q^d,\quad T=Q^t,\quad U=Q^u,
\]
\[
 C_m(q;t,u)=x^u\sum_{k=0}^m
 \frac{(Q^{-m};Q)_k(B^2Q^{m+1};Q)_k(U^{-1};Q)_kQ^k}
 {(BQ;Q)_k(T^{-1};Q)_k(Q;Q)_k},\quad
 (a;Q)_k=\prod_{r=0}^{k-1}(1-aQ^r).
 \tag{2}
\]
The physical vectors in \(\mathbb C^{t+1}\) are
\[
 C_u=C_j(q_0;t,u),\qquad
 w_u=\frac{D C_j(q_0;t,u)-D C_l(q_0;t,u)}{-2N\Delta_j},
 \quad D=q\partial_q,\quad
 \Delta_j=q_0^{2j+1}-q_0^{-2j-1}.
 \tag{3}
\]
The derivative fixes \(N,t,u\). It retains the large generic partner,
all original scalar factors, and the actual eigenvalue-gap derivative.
Let \(\widehat C(u)\) denote the same finite continuation in (2).

Use the physical Hermitian product
\(\langle v,z\rangle=\sum_{u=0}^t\overline{v_u}z_u\), and define
\[
 \alpha_N=\frac{\langle C,w\rangle}{\|C\|^2},\qquad
 w^\perp=w-\alpha_N C,\qquad
 X_u=\frac{u-u_0}{\sqrt N}.
 \tag{4}
\]
This is a change of basis in the actual value–normal plane.
It is not a quotient deleting the normal.

Fix a real compact interval \(I\Subset(1/2,1)\). There is a fixed
\(\delta_I>0\) such that the following estimates hold uniformly for
\(\tau\in I\) and the pairs (1) with \(1\le s\le\delta_I N\), at all
sufficiently large levels. All constants below may depend on \(I\).
Use the following coefficients:
\[
 \begin{gathered}
 b=\sin(\pi\xi),\quad c=\cos(\pi\tau),\quad
 \varpi=\sqrt{1-2c+\cos^2(\pi\xi)},\\
 \lambda=\frac{2\pi b}{\varpi},\qquad
 p=2\arctan(\varpi/b),\qquad
 a=\frac{i}{4b\varpi},\qquad
 \gamma=\frac{|a|^2}{2\lambda}
              =\frac1{64\pi b^3\varpi}.
 \end{gathered}
 \tag{5}
\]
In particular \(\lambda,\gamma\) stay between positive constants.

The full physical column measure has Gaussian moments:
\[
 \frac{\|C\|^2}{|\widehat C(u_0)|^2\sqrt N}
       =\sqrt{\frac{\pi}{\lambda}}+O(N^{-1/2}),\qquad
 \frac{\sum_u X_u^2|C_u|^2}{\|C\|^2}
       =\frac1{2\lambda}+O(N^{-1/2}).
 \tag{6}
\]
The corresponding convergence holds for every fixed polynomial
moment. Its first moment is exactly zero. For the actual normal,
\[
 \alpha_N=R_N(\tau,\tau/2)+O(1),\qquad
 \left\|w^\perp-a(u-u_0)C\right\|\le C_I\|C\|,
 \quad R_N(\tau,\nu)=w(N\nu)/C(N\nu).
 \tag{7}
\]
Consequently
\[
 \boxed{\quad
 \frac{\|w^\perp\|^2}{N\|C\|^2}
       =\gamma+O(N^{-1/2}),\qquad
 \det\operatorname{Gram}(C,w)
       =N\gamma\|C\|^4(1+O(N^{-1/2})).
 \quad}
 \tag{8}
\]
Thus the Gram of
\[
             \frac1{\|C\|}
               \left(C,\frac{w^\perp}{\sqrt{N\gamma}}\right)
 \tag{9}
\]
is \(\operatorname{diag}(1,1+O(N^{-1/2}))\). This retains both
actual columns and their full physical supports.

## 2. An exact Gaussian upper tail on the entire physical support

The magnetic polynomial [M] supplies the source-exact factorization
\[
 \widehat C(u)=x^u U^{-j}G_t(U),\qquad
 G_t(q_0^t z)=c_t B_h(z)A_n(z),
 \quad h=d-t,\quad n=t+j-d,
 \tag{10}
\]
where \(c_t\ne0\), all coefficients of \(A_n\) are positive, and
\[
 B_h(z)=\prod_{r=0}^{h-1}
                (1+q_0^{h-1-2r}z).
\]
Only the coefficient positivity is needed here; the stronger
negative-root statement in [M] is not required for this estimate.
For a physical \(u\), set
\(\theta=2\pi(u-u_0)/N\), so \(U=q_0^t e^{i\theta}\).
All prefactors outside \(B_h A_n\) in (10) have modulus one
apart from the same constant \(c_t\), also at \(u_0\).
Positivity gives \(|A_n(e^{i\theta})|\le A_n(1)\).

Pair the factors of \(B_h\) with phases \(\beta,-\beta\).
Since \(|\theta|\le\pi t/N\), \(|\beta|\le\pi(h-1)/N\), their
sum is strictly less than \(\pi\). The normalized pair modulus is
\[
 \frac{\cos((\theta+\beta)/2)\cos((\theta-\beta)/2)}
             {\cos^2(\beta/2)}
   =1-\frac{\sin^2(\theta/2)}{\cos^2(\beta/2)}
   \le\cos^2(\theta/2).
 \tag{11}
\]
It is nonnegative on this domain. If \(h\) is odd the remaining
central factor has ratio \(\cos(\theta/2)>0\). Therefore, including
the cases \(h=0,1\),
\[
 \frac{|C_u|}{|\widehat C(u_0)|}
       \le \cos(\theta/2)^h
       \le \exp(-h\theta^2/8).
 \tag{12}
\]
For \(\tau\in I\), \(h\ge c_I N\) at large levels. Hence
\(|C_u/\widehat C(u_0)|\le e^{-c_I X_u^2}\) on every physical index.
This global bound uses neither an independent maximization nor a
replacement of the original oscillatory column by positive coefficients.

The exact physical reflection [G] also gives
\[
 C_{t-u}=C_t\overline{C_u},\qquad |C_t|=1.
 \tag{13}
\]
Thus \(|C_{t-u}|=|C_u|\), and the physical probability measure in
(6) has mean \(u_0\) exactly, including half-integral centers.

## 3. The full ordinary Gaussian

On a fixed complex neighborhood of the center curve, [P] gives
\[
 \widehat C(N\nu)=N^{-1/2}{\cal B}_\xi(\tau,\nu)
                 e^{N\Phi_\xi(\tau,\nu)}(1+O(N^{-1})),
 \tag{14}
\]
with a nonzero holomorphic amplitude and all fixed relative-error
derivatives. The actual \(\xi=j/N\) stays in both coefficient functions.
Its selected magnetic multiplier is
\[
 e^{\Phi_\nu}
 =\frac{(bz+i\sqrt{1-2cz+\cos^2(\pi\xi)z^2})^2}
              {1-2cz+z^2},\qquad z=e^{\pi i(\tau-2\nu)}.
\]
At the real center \(z=1\), direct differentiation gives
\[
       \Phi_\nu=ip,\qquad \Phi_{\nu\nu}=-\lambda.
 \tag{15}
\]
For example \(z\partial_z\log(e^{\Phi_\nu})=-ib/\varpi\)
there; multiplication by \(-2\pi i\) gives the second identity.
The source logarithm chooses \(0<p<\pi\).

Taylor expansion of (14), divided by its value at \(u_0\), yields
on \(|X_u|\le N^{1/12}\)
\[
 C_u=\widehat C(u_0)e^{ip(u-u_0)}e^{-\lambda X_u^2/2}
       \left[1+O\!\left(N^{-1/2}(1+|X_u|^3)\right)\right].
 \tag{16}
\]
The remainder with its Gaussian factor is bounded by
\(C N^{-1/2}(1+|X_u|^3)e^{-c X_u^2}\), after decreasing \(c>0\).
This follows from bounded third derivatives on a fixed neighborhood;
the cubic exponent is \(O(N^{-1/2}|X_u|^3)\), uniformly small
on this window. The amplitude ratio has the same type of bound.
Outside it, (12) gives an exponentially small tail even after
multiplication by any fixed power of \(N\) or \(X_u\).

Gaussian Riemann sums of spacing \(N^{-1/2}\) now prove (6) and
all fixed moment statements. Their error is \(O(N^{-1/2})\):
for each Gaussian times a fixed polynomial, compare the integral
on each cell with its center value and integrate the absolute
derivative. The far ends of the finite physical support cost \(e^{-cN}\).

## 4. Orthogonalization exposes the actual normal mode

On a fixed buffered neighborhood of the center, [N, equation (30)]
proves, for some positive fixed \(\delta_I\),
\[
 \partial_\nu R_N=N\,\partial_\nu{\cal F}_\xi+O(1),\qquad
 \partial_\nu{\cal F}_\xi
     =\frac{iz}{4b\sqrt{1-2cz+\cos^2(\pi\xi)z^2}}.
 \tag{17}
\]
All fixed derivatives have the same bounded remainder after buffering.
In particular its center value is \(a\) in (5). Integrating (17)
and Taylor expanding its explicit coefficient gives, whenever
\(|u-u_0|\le\eta_I N\),
\[
 R_N(\tau,u/N)-R_N(\tau,\tau/2)
       =a(u-u_0)
          +O_I\!\left(\frac{|u-u_0|}{N}
                        +\frac{(u-u_0)^2}{N}\right).
 \tag{18}
\]
No estimate of the unknown magnetic-constant component of \(R_N\)
is used to obtain this formula.

There is no uncontrolled normal tail. On the whole physical grid,
[G] proves \(|R_N|\le C_I N^4\). At the center [N] proves
\(|R_N|\le C_I N\). Equations (12) and (6) therefore make the
contribution of \(|u-u_0|>\eta_I N\) exponentially small in every
norm or mean used below. On the central range the error in (18)
is bounded by \(C_I(1+X_u^2)\), whose fixed moments are bounded by
section 3. Exact symmetry (13) cancels the mean of its linear term.
Averaging (18) against \(|C_u|^2/\|C\|^2\) proves the first part
of (7). Subtract that mean; the same moment estimates prove its
second part. Combining with the second moment in (6) proves (8).

For an explicit full-profile formulation, use cells of length
\(N^{-1/2}\) centered at \(X_u\), set a vector to zero off its
physical cells, and define the isometry
\[
 ({\cal E}_{N,p}v)(x)
       =N^{1/4}e^{-ip(u-u_0)}v_u
       \quad\hbox{on the cell centered at }X_u.
 \tag{19}
\]
The phase removal is discrete and constant on each cell.
Let \(g_\lambda(x)=(\lambda/\pi)^{1/4}e^{-\lambda x^2/2}\), and let
\(\omega_N=\widehat C(u_0)/|\widehat C(u_0)|\).
Equations (7),(16) and the Gaussian cell estimate give
\[
 \begin{split}
 \left\|{\cal E}_{N,p}
           \frac{\overline\omega_N C}{\|C\|}-g_\lambda\right\|_{L^2}
       &\le C_I N^{-1/2},\\
 \left\|{\cal E}_{N,p}
       \frac{\overline\omega_N w^\perp}{\sqrt{N\gamma}\|C\|}
                -i\sqrt{2\lambda}\,xg_\lambda\right\|_{L^2}
       &\le C_I N^{-1/2}.
 \end{split}
 \tag{20}
\]
These are the zeroth and first normalized Gaussian–Hermite modes,
with the actual normal's factor \(i\) retained.

The uncentered Gram has the exact form
\[
 \frac{\operatorname{Gram}(C,w)}{\|C\|^2}
   =\begin{pmatrix}
       1&\alpha_N\\
       \overline{\alpha_N}&|\alpha_N|^2+\|w^\perp\|^2/\|C\|^2
     \end{pmatrix}.
 \tag{21}
\]
The full calibration [N] gives
\(\alpha_N/N={\cal F}_\xi(\tau,\tau/2)+o(1)\), a uniformly nonzero
quantity after decreasing \(\delta_I\). Thus its two eigenvalues
have orders \(N^2\) and \(N^{-1}\), respectively. Its condition
number has order \(N^3\); the two-column frame condition has order
\(N^{3/2}\). Centering and scaling in (9) explicitly removes this
polynomial distortion.

## 5. The value Gram across nearby channels

Fix \(R>0\), the same physical degree \(t/N=\tau\in I\), and allow
all complete pairs (1) with \(s\le R N^{3/4}\). This concerns only
ordinary columns and follows from [P,M]; no normal estimate is
being extended to a new degree domain. Put
\[
 \begin{gathered}
 r_j=s^2/N^{3/2},\quad
 \varpi_0=\sqrt{1-2\cos(\pi\tau)},\quad
 \lambda_0=2\pi/\varpi_0,\quad
 p_0=2\arctan\varpi_0,\quad
 \beta_0=\pi^2/(4\varpi_0),\\
 \psi_j=\overline{\omega_j}\,C_j/\|C_j\|,\qquad
 \omega_j=\exp\{i\pi[d(t-j)+j^2]/(2N)\}.
 \end{gathered}
 \tag{22}
\]
The phase \(\omega_j\) is the exact center phase in [M], not a
freely chosen relative channel character. Use the common discrete
carrier isometry \({\cal E}_{N,p_0}\). Uniformly over this family,
\[
 \|{\cal E}_{N,p_0}\psi_j-g_{r_j}\|_{L^2}
       \le C_{I,R}N^{-1/2},\qquad
 g_r(x)=\left(\frac{\lambda_0}{\pi}\right)^{1/4}
                   e^{-\lambda_0x^2/2+i\beta_0rx}.
 \tag{23}
\]
Indeed set \(D_\xi=\cos^2(\pi\xi)\). At the center,
\(\partial_{D_\xi}p=1/(b\varpi)\). Since
\(\xi=1/2-(s+1)/(2N)\), Taylor expansion gives
\[
 \sqrt N(p-p_0)=\beta_0 r_j+O_{I,R}(N^{-1/2}),\qquad
 \lambda-\lambda_0=O_{I,R}(N^{-1/2}).
 \tag{24}
\]
The omitted \(2s+1\) in \((s+1)^2\) contributes \(O(N^{-3/4})\);
the quadratic remainder in \(D_\xi\) contributes \(O(N^{-1/2})\).
Use (16), (12) and the same moment bounds to obtain (23).
Gaussian integration consequently gives the source-specific
entrywise Gram formula
\[
 \boxed{\quad
 \langle\psi_j,\psi_k\rangle
   =\exp\!\left[-\frac{\pi^3(r_j-r_k)^2}{128\varpi_0}\right]
                      +O_{I,R}(N^{-1/2}).
 \quad}
 \tag{25}
\]
For \(s\le M\sqrt N\), all these phase-normalized unit columns
are \(O_{I,M}(N^{-1/2})\) from the same full Gaussian. In
particular they are not a uniformly separated orthogonal channel
frame on that window. An entrywise error for a growing family
does not give a lower bound for its smallest Gram eigenvalue.

## 6. The exact adjoint carrier has a tame doubled pairing

There is also an exact gluing consequence for these particular
full physical packets. Set \(q=q_0\),
\[
 \begin{gathered}
 c_j=q^{2j+1}+q^{-2j-1},\quad
 P_t(Z)=\prod_{m=0}^t(Z-c_m),\quad
 Q_{t,j}(Z)=P_t(Z)/(Z-c_j)^2,\\
 B_t=(-1)^t\left(\prod_{r=1}^t2\sin(\pi r/N)\right)^2,\quad
 \nu_j=(-1)^j q^{j(j+1)},\\
 \sigma_{t,j}=x^t\nu_j Q_{t,j}(c_j)/B_t,\qquad
 \eta_{t,j}=-\frac{s}{2\Delta_j}
                    +\frac{Q_{t,j}'(c_j)}{Q_{t,j}(c_j)} .
 \end{gathered}
 \tag{26}
\]
The complete actual Hermite identity [H] is
\[
 C^{\mathsf T}C=0,\qquad
 C^{\mathsf T}w=\sigma_{t,j},\qquad
 w^{\mathsf T}w=\sigma_{t,j}\eta_{t,j},\qquad
 |\eta_{t,j}|\le C N^3 .
 \tag{27}
\]
Transpose here has no conjugation. All phases in \(\sigma_{t,j}\)
are retained.

Put \(d_N=\|w^\perp\|/\|C\|\), \(e_0=C/\|C\|\),
\(e_1=w^\perp/(\|C\|d_N)\), and \({\cal U}=(e_0,e_1)\).
These two vectors are exactly Hermitian orthonormal. Formula (27)
gives their exact bilinear Gram
\[
 {\cal B}={\cal U}^{\mathsf T}{\cal U}
 =\frac{\sigma_{t,j}}{\|C\|^2d_N}
   \begin{pmatrix}
      0&1\\1&(\eta_{t,j}-2\alpha_N)/d_N
    \end{pmatrix}.
 \tag{28}
\]
The native energy in [E] is precisely
\(E_{t,j}=\|C\|^2/|\sigma_{t,j}|\). It has
\(\log E_{t,j}=N e(\tau,\xi)+O(\log N)\), uniformly near the fold
on our real degree compact. Its folded profile is positive
throughout \(1/2\le\tau\le1\), starting at \(v_8/(2\pi)>0\)
and increasing. Continuity in \(\xi\) therefore allows a further
fixed decrease of \(\delta_I\) so that \(e(\tau,\xi)\ge c_I>0\).
Use (8), \(\alpha_N=O_I(N)\), and (27) in (28). For some \(a_I>0\),
\[
                       \|{\cal B}\|\le C_I e^{-a_I N}.
 \tag{29}
\]
Thus pairing two copies of this same carrier bilinearly is
exponentially small, despite its positive Hermitian Gram.

Retain instead both this actual carrier and its complex conjugate:
\({\cal D}=({\cal U},\overline{\cal U})\). Exact matrix identities give
\[
 {\cal D}^*{\cal D}
   =\begin{pmatrix}I&\overline{\cal B}\\{\cal B}&I\end{pmatrix},
 \qquad
 {\cal D}^{\mathsf T}{\cal D}
   =\begin{pmatrix}{\cal B}&I\\I&\overline{\cal B}\end{pmatrix}.
 \tag{30}
\]
Their respective limits are \(I_4\) and the two-by-two block swap,
with exponentially small errors. In particular the doubled physical
frame and this bilinear pairing have bounded condition numbers for
large levels. No original normal direction was removed to get this.

Its operator type matters. The original physical Casimir block
\(\Omega_t\) is complex symmetric, and
\[
 \Omega_t{\cal U}
   ={\cal U}\begin{pmatrix}c_j&d_N^{-1}\\0&c_j\end{pmatrix},
 \qquad
 \Omega_t^*\overline{\cal U}
   =\overline{\cal U}
       \begin{pmatrix}c_j&d_N^{-1}\\0&c_j\end{pmatrix}.
 \tag{31}
\]
The conjugate vectors are an actual adjoint-Casimir carrier, not
additional eigenchannels of \(\Omega_t\). Formula (30) is an exact
adapter when those two stated boundary types are paired. It does
not assert that an arbitrary original crossing, turn, cap or
partial filling produces the adjoint carrier on the other side.

## 7. What the Gram does and does not change

The magnetic energy calculation [E] already gives exact Fourier
norm comparisons and its original center action. A separate
initialized-meridian-row calculation in the research ledger
constructs fixed-order Gaussian jet Grams for a different source.
Here the vectors are the ordinary and actual generic-confluent
q-Hahn columns (3), and (12) controls their complete physical tails.
Their particular normal direction and the cross-channel scale
in (25) are computed from these original source equations.

The Hermitian Gram above is not the bilinear complete
Christoffel–Darboux gluing matrix. Original inverse rows, its
measure and phase, the marked closing, turns, and external
normalizations must be transported through any basis change.
No cap is asserted to be the Hermitian adjoint of a cup.
The statement also excludes the physical endpoint \(t=N-1\)
as a uniform degree family and excludes the isolated simple channel.

This supplies full-packet norm and transverse-normal information.
It does not estimate the sum over distinct Casimir nodes, match
geometric packets across an arbitrary short component, or prove
a nonzero original scalar after closing. No new knot-volume case
or finite-exception theorem follows without those further estimates.

The complete selected proof and closest-coverage texts are:

| Label | Complete text | SHA256 |
| --- | --- | --- |
| N | [Calibrated actual normal](research_q_hahn_calibrated_normal_transport.md), 582 lines | 07cd14b27ac3743ab28995d4debabae8e54867cd13b72dc2c250a3555618e0a5 |
| P | [Full physical ordinary packet](actual_q_hahn_full_physical_complex_packet.md), 338 lines | 28b7088c4cc947f05d2e395759b77c1232e150dba734d6dca3610548f15b1e0c |
| G | [Physical-grid actual normal](actual_q_hahn_physical_partner_normal_bound.md), 232 lines | 0725b210bd16899260533cf7a1a7aa9602a7ed0b0e18baf4831efb7a968e07d3 |
| M | [Exact magnetic polynomial](actual_q_hahn_magnetic_complex_corridor.md), 418 lines | 6e55386df86acedef28345ad31cfc4b149ea66b355d26bd3fc3dfa0af7d644de |
| E | [Native magnetic energy profile](actual_matching_edge_magnetic_energy_profile.md), 365 lines | b6eda690e606aa3581280f4b8c623ee85c178c759c3c8588b4d5b338d1e6f91a |
| H | [Complete actual Hermite packet](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_complete_casimir_hermite_packet.md), 321 lines | a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c |

Only written mathematics, complete text reads and metadata hashes
were used. Earlier final notes, the manuscripts and the ledger
were not changed.
