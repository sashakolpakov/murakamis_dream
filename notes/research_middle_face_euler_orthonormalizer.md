# The literal middle Euler factor is a full boundary orthonormalizer

21 November 2026. Research note. Earlier final notes and the public
manuscripts remain unchanged.

The finite Euler factor already present in the middle five-point
description of a crossing also supplies the correct orthonormal
coordinates for its complete middle-weight boundary packet. In these
coordinates the genuine turn is index reversal, and the conjugated
middle face clock is the ordinary diagonal clock. Both original packet
closings are coordinate rows. The literal marked cap used in the
five-point identity is a different functional; its factorial row is
retained explicitly below.

The positive Gram and the Newton crossing intertwiner were established
previously. The result here identifies their orthonormalizer with an
actual factor of the original face operator identity. It also gives
the exact transport of the complete source circuit and its previously
constructed Gaussian windows. It does not make a geometric contour
positive or prove a volume estimate.

## 1. The actual strict Euler argument

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and

\[
 x=-q^{-1},\qquad F_r=(Q;Q)_r=\prod_{j=1}^r(1-Q^j),\qquad
 \nu_r=(-1)^rQ^{r(r+1)/2},\qquad F_0=1.
 \tag{1}
\]

Write \({r\brack a}_Q=F_r/(F_aF_{r-a})\) for \(0\le a\le r\le d\).
All factorial indices below lie between zero and \(d\). On the faithful
middle-weight space use the original physical basis

\[
 v_r=|r,d-r\rangle,\quad 0\le r\le d,\qquad Zv_r=Q^rv_r.
 \tag{2}
\]

The cyclic face unit is \(X=xS_2S_1^{-1}\), with the actual nonzero
marks \(S_1^N=\mu\), \(S_2^N=x^N\mu\). Thus

\[
 Xv_r=xv_{r-1}\quad(r\ge1),\qquad Xv_0=x^{N+1}v_d.
 \tag{3}
\]

The literal middle five-point argument and Euler polynomials are

\[
 n=(Q-Z^{-1})X,\qquad
 P_Q(B)=\sum_{h=0}^d\frac{(-1)^hQ^{h(h-1)/2}B^h}{F_h},\qquad
 V_Q(B)=\sum_{h=0}^d\frac{B^h}{F_h}.
 \tag{4}
\]

For \(B^N=0\), the finite binomial identity gives

\[
 P_Q(B)V_Q(B)=V_Q(B)P_Q(B)=I.
 \tag{5}
\]

Indeed the coefficient of \(B^m\), for \(1\le m<N\), is

\[
 \frac1{F_m}\sum_{h=0}^m(-1)^hQ^{h(h-1)/2}{m\brack h}_Q
                  =\frac{(1;Q)_m}{F_m}=0;
\]

terms of higher degree vanish. No infinite product is specialized.
Put

\[
 \mathsf L v_r=(1-Q^r)v_{r-1}\quad(r\ge1),\qquad
 \mathsf L v_0=0,\qquad D_\nu=\operatorname{diag}(\nu_r).
\]

The literal operator in (4), including its missing arrow, is

\[
 \boxed{\quad n=q\mathsf L Z^{-1},\qquad
 D_\nu\mathsf L D_\nu^{-1}=-\mathsf L Z^{-1}.\quad}
 \tag{6}
\]

For the first equality, at input \(r\ge1\) the coefficient in (4) is

\[
 x(Q-Q^{-(r-1)})=qQ^{-r}(1-Q^r).
\]

At input zero it vanishes, since \(Q-Q^{-d}=0\), even though (3)
has a nonzero wrap. For the second equality use

\[
                    \nu_{r-1}/\nu_r=-Q^{-r}.
\]

Both sides kill \(v_0\). In particular \(n^N=0\) exactly. Neither
the cyclic wrap of \(X\) nor the strict endpoint of \(n\) has been
discarded.

## 2. The exact turn and boundary metric

Write \(\mathsf Rv_r=v_{d-r}\) for index reversal, and let
\(C\) be the cyclic-column matrix of the complete Casimir packet.
The preceding turn theorem proves

\[
 C=D_\nu V_Q(-q\mathsf L),\qquad
 \mathcal J=C\mathsf R C^{-1},\qquad
 G=(C^{-1})^*C^{-1}.
 \tag{7}
\]

Here \(G\) is the positive boundary Gram; it is distinct from every face
clock below. Its inner product is conjugate-linear in the first input.

**Theorem 1.** Define \(\mathcal E=P_Q(n)\). Then, at every level
and every retained index,

\[
 \boxed{\begin{gathered}
 C=\mathcal E^{-1}D_\nu,\qquad
 G=\mathcal E^*\mathcal E,\qquad
 \mathcal J=\mathcal E^{-1}\mathsf R\mathcal E,\\
 \|y\|_G=\|\mathcal Ey\|_2.
 \end{gathered}}
 \tag{8}
\]

**Proof.** Equation (6) and finite polynomial conjugation give

\[
 D_\nu V_Q(-q\mathsf L)D_\nu^{-1}=V_Q(n)=\mathcal E^{-1}.
\]

This proves the first identity. Moreover

\[
 \frac{\nu_{d-r}}{\nu_r}
   =(-1)^dQ^{Nd/2-Nr}=1,
 \tag{9}
\]

because \(Q^{Nd/2}=(-1)^d\). Thus \(D_\nu\) commutes with
\(\mathsf R\). Substitution in (7) gives the turn identity.
Since \(D_\nu\) is unitary, \(C^{-1}=D_\nu^{-1}\mathcal E\)
gives the Gram and norm identities. \(\square\)

The factor \(\mathcal E\) is prescribed by an actual crossing
factorization and is independent of a chosen knot exterior. It need
not be unitary or polynomially conditioned in the flat physical basis.
Its role is an isometry from the stated Gram to Euclidean coordinates.

## 3. The original packet closings and the literal marked cap

For a whole Hopf box \(f(\Omega_d)\), write

\[
 y=f(\Omega_d)v_0=C\alpha,
\]

where \(\alpha\) is its full Newton coefficient vector, including
every repeated-root derivative. The original packet rows satisfy

\[
 m_{\rm pkt}y=\alpha_0,\qquad \phi_{\rm pkt}y=\alpha_d.
\]

Since \(\mathcal EC=D_\nu\) and \(\nu_0=\nu_d=1\),

\[
 \boxed{\quad
 m_{\rm pkt}=e_0^{\mathsf T}\mathcal E,\qquad
 \phi_{\rm pkt}=e_d^{\mathsf T}\mathcal E=e_d^{\mathsf T}.
 \quad}
 \tag{10}
\]

Both have exactly unit dual norm in \(G\). Also

\[
 \mathcal Ev_0=v_0,\qquad e_d^{\mathsf T}\mathcal E=e_d^{\mathsf T}.
\]

Consequently the outer-entry source has, for every middle-block
matrix \(A\), the exact invariance

\[
             (\mathcal EA\mathcal E^{-1})_{d0}=A_{d0}.
 \tag{11}
\]

For a whole Hopf box, \(A_{d0}=\phi(f)\), by the cyclic-column
formula. This is the reconstructed source, not the all-array averaged
trace on the original two physical heads.

The literal five-point identity also has its own explicitly specified
cup and marked cap:

\[
 p=N\sum_{a=0}^d x^{a-d}v_a,\qquad
 m_{\rm lit}(v_a)=x^{d-a}/N^2,\qquad m_{\rm lit}p=1.
 \tag{12}
\]

Its transformed boundary data are

\[
 \boxed{\quad
 \mathcal Ep=Ne_d,\qquad
 (m_{\rm lit}\mathcal E^{-1})_r
      =\frac{x^d(-q)^r\nu_r^{-1}F_r}{N^2}.
 \quad}
 \tag{13}
\]

To verify every coefficient, use the known complete matrix

\[
 C_{ar}=\nu_a(-q)^{r-a}{r\brack a}_Q\quad(a\le r).
\]

Its last column is \(C_{ad}=(-q)^{d-a}=x^{a-d}\), since
\({d\brack a}_Q=\nu_a^{-1}\). Thus \(p=NCe_d\), proving
the first formula of (13). For the second use

\[
 \sum_{a=0}^r\nu_a{r\brack a}_Q
   =\sum_{a=0}^r(-1)^aQ^{a(a-1)/2}Q^a{r\brack a}_Q
   =(Q;Q)_r=F_r,
\]

and \(\mathcal E^{-1}=CD_\nu^{-1}\). In particular the
transformed cap's last entry is \(1/N\), retaining the pairing in
(12). Its squared Euclidean norm is

\[
             \|m_{\rm lit}\mathcal E^{-1}\|_2^2
                         =N^{-4}\sum_{r=0}^d|F_r|^2.
 \tag{14}
\]

It is not the coordinate row in (10). An identification of these two
typed caps would lose the very factorial boundary factors needed in
the original five-point source.

The transformed literal row, denoted by \(\lambda_r\), also has the
exact pointed recurrence

\[
 \lambda_{r+1}=q(Q^{-r-1}-1)\lambda_r\quad(0\le r\le d),
 \qquad \lambda_0=x^d/N^2,\qquad \lambda_N=0.
 \tag{14a}
\]

It follows by taking consecutive ratios in (13); at \(r=d\) the
displayed coefficient is zero. Thus its amplitude, phase and both
endpoints are fixed. Replacing this zero extension by a cyclic wrap
would insert the nonzero current \(\lambda_0\).

## 4. The conjugated clock is the actual geometric face clock

The literal middle identity defines

\[
 \mathcal H=\mathcal E^{-1}Z\mathcal E=Z(1-n),\qquad
 \mathcal F_{\mathcal H}=\mathcal E^{-1}\mathcal F_Z\mathcal E,
 \qquad
 \mathcal F_Z=\varpi_N\operatorname{diag}(F_r^{-1}),
 \tag{15}
\]

where
\[
 \varpi_N=\sqrt N\exp\!\left\{i\pi\left[
              \frac14-\frac{N+N^{-1}}{12}\right]\right\}.
\]

This is the original marked scalar, of modulus \(\sqrt N\).
These equalities include the original logarithmic
lifts. For completeness, \(nZ=QZn\) and the finite recurrence

\[
                 P_Q(Qn)(1-n)=P_Q(n)
\]

give \(\mathcal E\mathcal H=Z\mathcal E\) directly. The
highest coefficient of that recurrence is harmless because \(n^N=0\).
Since \(\mathsf RZ\mathsf R=Q^{-1}Z^{-1}\), Theorem 1 gives

\[
 \boxed{\quad
 \mathcal E\mathcal H\mathcal E^{-1}=Z,\qquad
 \mathcal J\mathcal H\mathcal J^{-1}=Q^{-1}\mathcal H^{-1},\qquad
 \mathcal E\mathcal F_{\mathcal H}\mathcal E^{-1}=\mathcal F_Z.
 \quad}
 \tag{16}
\]

The classical symbol \(\mathcal H_{\rm cl}=X+Z-XZ\) is the
cross-ratio of the actual developed middle five-point configuration.
Thus the diagonal register is tied to this specific face clock, rather
than assigned a new classical meaning. The simple clock does not make
the Casimir semisimple: \(\mathcal E\) is invertible on all \(N\)
coordinates and retains every Casimir normal.

On the literal cup, (13)--(16) give

\[
 \mathcal Hp=Q^{-1}p,\qquad
 \mathcal F_{\mathcal H}p=(\varpi_N/N)p.
 \tag{17}
\]

The top marked clock value and all factors \(N,\varpi_N\) therefore
agree with the original five-point source. The diagonal entries
\(\varpi_N/F_r\) in (15) are retained; diagonalization has not
bounded their sizes.

## 5. Whole gates, the quartic source problem, and coherent windows

Let \(M\) be the original full Newton bilinear product and \(\ell\)
an original closing row. For a packet \(y=\Xi_N(f)=C\alpha\),

\[
                         \mathcal E\Xi_N(f)=D_\nu\alpha.
 \tag{18}
\]

Hence in the new orthonormal coordinates a binary gate is exactly

\[
 \widehat M(u,v)=D_\nu M(D_\nu^{-1}u,D_\nu^{-1}v),
 \qquad \widehat\ell=\ell D_\nu^{-1}.
 \tag{19}
\]

Leaves and every other typed map are transported in the same way;
the turn remains reversal by (9). These unitary changes preserve
Hilbert--Schmidt tensor norms and all normalization budgets. They map
unit balls onto unit balls and preserve each squared residual. Thus
the normalized quartic minimization problem has exactly the same
degree, feasible set up to unitary coordinates, objective values and
minimum as in Newton coordinates. No global unknown scalar is used
to choose these coordinates. All original Cartan, framing and
peripheral factors remain attached.

An individual face factor need not be a Hopf box. It is transported
as the full matrix \(A\mapsto\mathcal EA\mathcal E^{-1}\), in
its original position. Equation (19) is not permission to replace
such a factor by the polynomial reconstructed from one cyclic column.

The previously constructed Gaussian resolution has a direct face
interpretation as well. For fixed \(\sigma>0\), put

\[
 g_{\xi,z}(r)=\left(\frac{N}{\pi\sigma}\right)^{1/4}
 e^{-(r-N\xi)^2/(2\sigma N)}(z/q)^r,\qquad
 \psi_{\xi,z}=\mathcal E^{-1}g_{\xi,z},
 \quad \xi\in\mathbb R,\quad |z|=1.
 \tag{20}
\]

With \(d\mu=d\xi\,d\arg z/(2\pi)\), its exact full-dimensional
resolution becomes

\[
 y=\int\psi_{\xi,z}\langle\psi_{\xi,z},y\rangle_G\,d\mu,
 \qquad
 \int|\langle\psi_{\xi,z},y\rangle_G|^2d\mu=\|y\|_G^2.
 \tag{21}
\]

The finite Fourier integral makes the original resolution diagonal,
and the remaining Gaussian integral equals one. Pulling it back by
the isometry \(\mathcal E\) proves (21). The actual turn, including
its phase and endpoint centers, obeys

\[
 \mathcal J\psi_{\xi,z}
       =(z/q)^d\psi_{d/N-\xi,Q/z}.
 \tag{22}
\]

This follows by reversing the entries in (20). The two packet
closings on these same states are exactly

\[
 m_{\rm pkt}\psi_{\xi,z}
       =\left(\frac{N}{\pi\sigma}\right)^{1/4}
                                e^{-N\xi^2/(2\sigma)},
\]
\[
 \phi_{\rm pkt}\psi_{\xi,z}
       =\left(\frac{N}{\pi\sigma}\right)^{1/4}
          e^{-(d-N\xi)^2/(2\sigma N)}(z/q)^d.
 \tag{23}
\]

The Gaussian resolution, reversal law and endpoint functions are
existing constructions. Here the Gaussian entries are in Euler
orthonormal coordinates. The literal pullback of a Newton window is
instead \(Cg_{\xi,z}=\mathcal E^{-1}D_\nu g_{\xi,z}\); it too gives
an exact resolution. Reversal and endpoint laws agree because
\(D_\nu\) commutes with reversal and fixes both endpoints.
One-crossing formulas in Newton coordinates must be conjugated as in
(19), rather than reused unchanged on the windows (20).
Equations (20)--(23) do not assert that a short tangle
outputs one of these states or that a geometric saddle has nonzero
coefficient in the prescribed closing.

## 6. Fixed-root and geometric scope

Every formula above is at the original \(q=e^{\pi i/N}\), for all
levels, including even and composite levels. Repeated-root Casimir
directions are retained. Derivatives of a generic quantum parameter
would require the actual parameter-dependent bend and scalar families;
the fixed-root identities do not supply those derivatives.

The finite Euler operator in (4) is the one already represented by
the original full-function circle-minus-radial coefficient functional.
Using (8) keeps that complete functional and every factorial/source
adapter. It does not select the circular component or erase a strict
wall. Positive definiteness of \(G\), or the resolution (21), also
does not imply entrywise positivity of the crossing kernels.

The separate classical companion gauge fixes the total lower Gauss
coordinate. The actual total raising and lowering operators change
physical total degree and are not separately endomorphisms of this
middle block. Thus (8) and (16) do not quantize the entire classical
companion-frame torsor or its seven rational charts. They identify
the particular preserved face clock and its complete boundary packet.

The result removes an unspecified boundary change of coordinates:
the needed isometry is a literal factor of the original face algebra.
The remaining geometric problem is to estimate the actual transported
packet and original source, with its phase and complementary regions.
No new volume identity or finite-exception theorem is inferred here.

## Complete proof sources and coverage

All three complete proof texts were read at matching pins. The first
supplies the actual cyclic-column matrix, Gram, turn and packet rows.
The second fixes the literal Euler argument, conjugated face clock
and marked five-point boundary. The third supplies the existing
Gaussian resolution and its exact endpoint transport.

| Source | SHA-256 |
|---|---|
| [Actual middle turn and boundary Gram](research_middle_weight_turn_gram_kernel.md) | 01f2c9d5724eca87c6bef1ffa8a6faae53f47d5dbdc7e71513165c39cb674e41 |
| [Literal middle operator and full source](literal_middle_full_phi_certificate.md) | 85681202cfdf788e251dafa560fcaad6468c7058c00c4b1d51f3695a497282d1 |
| [Existing Gaussian frame](research_gaussian_frame_newton_transport.md) | b6ed7fa19097323f76b0b22fb4fc7361b9d4e52c3f19d17c12d94c6fff623af9 |

The complete [middle five-point wall calculation](actual_middle_five_point_wall_factorization.md)
was also read for coverage at SHA-256
`a3c9d055fd2acc763f746113379987bfefddb46431a14577067dabb1a46dbcd7`.
Its factorization, actual flag coordinates and source walls precede
this note; no novelty is claimed for those constructions.

Only written mathematics and text/hash operations were used. No
mathematical program, test, numerical experiment, build, git operation
or earlier-final edit was performed.
