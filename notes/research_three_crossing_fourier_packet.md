# Almost invariance and a nonzero Fourier window in the original three-crossing column

Research note, 3 November 2026.

The original three-crossing column has a positive factorial envelope
after its specified quadratic phase is removed. This gives a quantitative
almost-invariant vector for a concrete unitary cyclic shift, and also a
nonzero Fourier coefficient with its full exponential and polynomial
normalization. The latter conclusion uses the positive envelope and its
Gaussian profile, not almost invariance alone.

The shift is a unitary auxiliary operator on the original Newton
coefficient space. It is not a unitarization of the original crossing
matrix. The final section keeps that distinction and identifies the
actual test vector whose overlap has been proved.

## 1. The actual source and its positive comparison vector

Fix \(N\ge2\), \(D=N-1\), and
\[
 q=e^{\pi i/N},\qquad Q=q^2,\qquad
 \kappa=\exp\!\left(\frac{\pi iD^2}{2N}\right),\qquad
 \alpha=M_N^3\mathbf e_0.
 \tag{1}
\]
Here \(M_N\) is the original crossing matrix with its carrier
scalar retained. Put
\[
 \begin{split}
 g_j&=S_j^2,\qquad
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\quad S_0=1,\\
 \mathsf D_N&=\operatorname{diag}\big(q^{j(j+2)}\big)_{j=0}^D,\\
 \beta&=\kappa^{-3}\mathsf D_N^{-1}\alpha,\qquad
 \omega_N=\exp\!\left(i\pi\left[\frac14+\frac1{4N}-\frac N{12}\right]\right).
 \end{split}                                                    \tag{2}
\]
The diagonal \(\mathsf D_N\) and both displayed scalar phases
are unitary in the ordinary Euclidean Newton metric.
The [full original coefficient profile](research_three_crossing_full_coefficient_profile.md),
Corollary 3, proves
\[
 \|\beta-\omega_N N^{-1/2}g\|_2
                  \le \frac{C}{N}\,N^{-1/2}\|g\|_2
 \tag{3}
\]
for all sufficiently large integer levels, including both parities.
No positivity of the actual complex coefficients is postulated.

Define the two unit vectors
\[
 u_N=\frac{g}{\|g\|_2},\qquad
 v_N=\frac{\omega_N^{-1}\beta}{\|\beta\|_2}.
 \tag{4}
\]
The normalization inequality applied to (3) gives
\[
                         \|v_N-u_N\|_2=O(N^{-1}).
 \tag{5}
\]
The exact source is therefore close to a specified positive
vector in a specified metric.

Throughout, write
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 x_0=\frac56,\qquad J_0=J(x_0),\qquad a=\pi\sqrt3.
 \tag{6}
\]
The function \(J\) has its unique global maximum on \([0,1]\)
at \(x_0\), with
\(J'(x_0)=0\), \(J''(x_0)=-a\), and \(J_0>0\).

## 2. The factorial Gaussian with its normalization

**Lemma 1.** Uniformly for \(j/N\) in a fixed compact
subinterval of \((0,1)\),
\[
 S_j^2=2N\sin(\pi j/N)\exp(2NJ(j/N))(1+O(N^{-1})).
 \tag{7}
\]
Consequently
\[
 \begin{split}
 \sum_{j=0}^D g_j
   &=N^{3/2}\sqrt{\frac{\pi}{a}}\,
               e^{2NJ_0}(1+O(N^{-1/2})),\\
 \|g\|_2
   &=N^{5/4}\left(\frac{\pi}{2a}\right)^{1/4}
               e^{2NJ_0}(1+O(N^{-1/2})).
 \end{split}                                                    \tag{8}
\]
For every fixed \(T<\infty\), uniformly over integers
\(|m|\le T\sqrt N\),
\[
 \frac1{\sqrt N}\sum_{j=0}^Dg_j e^{-2\pi imj/N}
  =N\sqrt{\frac{\pi}{a}}\,e^{2NJ_0}
       e^{-2\pi imx_0}e^{-\pi^2m^2/(aN)}
                    (1+O_T(N^{-1/2})).
 \tag{9}
\]

*Proof.* Subtract \(\log(2\pi t)\) from
\(\log(2\sin\pi t)\). The difference
\(\log(\sin\pi t/(\pi t))\) is smooth at zero.
Stirling's formula for \(j!\), followed by the trapezoidal
Euler--Maclaurin formula for this smooth difference, gives
\[
 \log S_j=NJ(j/N)+\tfrac12\log(2N\sin(\pi j/N))+O(N^{-1})
 \tag{10}
\]
on the stated compact interval. Exponentiation proves (7).
The same subtraction with an endpoint bound gives the
uniform estimate
\(\log S_j=NJ(j/N)+O(\log N)\) for \(0\le j<N\),
as also proved in the source profile note.
Since \(J\) has a strict maximum at \(x_0\), this bounds the
part outside any fixed neighborhood of \(x_0\) by a polynomial
times an exponentially smaller quantity.

Set \(s_j=(j-Nx_0)/\sqrt N\). On a fixed small neighborhood,
Taylor's formula and (7) give
\[
 \frac{g_j}{N e^{2NJ_0}}
       =e^{-a s_j^2}+
          O\!\left(N^{-1/2}(1+|s_j|^3)e^{-c s_j^2}\right)
 \tag{11}
\]
for a constant \(c>0\), uniformly there.
For example, choose the neighborhood so that the cubic
Taylor remainder in the exponent is at most
\(a s_j^2/4\); the inequality
\(|e^z-1|\le |z|e^{|z|}\) then gives (11).
The contribution outside this neighborhood is exponentially
small. The same estimate holds after squaring, with a
possibly different polynomial and \(c\).

The lattice \(s_j\) has spacing \(N^{-1/2}\).
For \(|m|/\sqrt N\le T\), the Riemann sum for
\(e^{-a s^2}e^{-2\pi i(m/\sqrt N)s}\) differs from its
integral by \(O_T(N^{-1/2})\), uniformly in the fractional
shift \(Nx_0\): its derivative has a uniformly bounded
integral. The Gaussian integral is
\[
 \int_{\mathbb R}e^{-a s^2}e^{-2\pi its}\,ds
                         =\sqrt{\pi/a}\,e^{-\pi^2t^2/a}.
 \tag{12}
\]
Summing (11) proves (9). This integral is bounded away
from zero for \(|t|\le T\), so the error can be written
relatively. The case \(m=0\) gives the first formula in
(8); applying the same argument to \(g_j^2\) gives the
second. No level residue class was selected. \(\square\)

In particular the positive coefficient mass has width
\(\sqrt N\) about the original index \(5N/6\).
For every bounded continuous function \(f\),
\[
 \sum_j |u_{N,j}|^2 f(s_j)
   \longrightarrow
        \sqrt{\frac{2a}{\pi}}
             \int_{\mathbb R}f(s)e^{-2as^2}\,ds.
 \tag{13}
\]
The same statement holds with \(u_N\) replaced by \(v_N\),
by (5). This assertion does not require an unbounded-moment
estimate for the error in (5).

## 3. Actual Fourier coefficients and almost invariance

Use the unitary discrete Fourier transform
\[
 \widehat z(m)=\frac1{\sqrt N}
                   \sum_{j=0}^Dz_j e^{-2\pi imj/N},
 \qquad m\in\mathbb Z/N\mathbb Z.
 \tag{14}
\]
Let \(\mathsf S_N z\) be the cyclic shift
\((\mathsf S_Nz)_j=z_{j-1\bmod N}\).

**Theorem 2.** For every fixed \(T<\infty\), uniformly over
integer representatives \(|m|\le T\sqrt N\), the actual
normalized source satisfies
\[
 \boxed{\quad
 \widehat v_N(m)=
   \left(\frac2{\sqrt3}\right)^{1/4}N^{-1/4}
       e^{-5\pi im/3}
       \exp\!\left(-\frac{\pi m^2}{\sqrt3 N}\right)
                         (1+O_T(N^{-1/2})).
 \quad}                                                         \tag{15}
\]
In particular \(|\widehat v_N(0)|\ge cN^{-1/4}\) for a
fixed \(c>0\) and all sufficiently large \(N\).
The same is true throughout each fixed Gaussian window,
with a constant depending on \(T\).
The original unnormalized, dechirped source has
\[
 \boxed{\quad
 \widehat\beta(m)=
      \omega_N\,3^{-1/4}N^{1/2}e^{2NJ_0}
       e^{-5\pi im/3}
       \exp\!\left(-\frac{\pi m^2}{\sqrt3 N}\right)
                         (1+O_T(N^{-1/2})).
 \quad}                                                         \tag{16}
\]
Its shift residual is
\[
 \boxed{\qquad
 \|\mathsf S_Nv_N-v_N\|_2
                  =\sqrt{\pi\sqrt3}\,N^{-1/2}+O(N^{-1}).
 \qquad}                                                        \tag{17}
\]
All conclusions hold along the full integer sequence of levels.

*Proof.* Divide (9) by the norm in (8). The resulting
constant is \((2\pi/a)^{1/4}=(2/\sqrt3)^{1/4}\), proving
(15) first for \(u_N\). The unitary Fourier transform and
(5) bound the difference of any two corresponding Fourier
coefficients by \(O(N^{-1})\). The leading term in (15)
has magnitude bounded below by \(c_TN^{-1/4}\) throughout
the stated window. Hence the source error is relatively
\(O_T(N^{-3/4})\), smaller than the error already in (9).
This proves (15) for the actual vector.
Applying the same argument directly to (3) proves (16).
In particular a possible coherent error has been bounded
before asserting that the coefficient is nonzero.

For (17), first use the exact factorial ratio
\[
  g_j/g_{j-1}=4\sin^2(\pi j/N)=:d_j
                         \qquad(1\le j<N).
 \tag{18}
\]
Near \(x_0\), \(d(x_0)=1\), \(d'(x_0)=-2a\), and
\[
       d_j^{-1}-1=2a\,s_j/\sqrt N+O(s_j^2/N).
 \tag{19}
\]
The argument proving (11)--(13), now including the fixed
polynomial weights in (19), gives
\[
 \begin{split}
 N\,\frac{\sum_{j=1}^D|g_{j-1}-g_j|^2}{\|g\|_2^2}
   &=
   4a^2\sqrt{\frac{2a}{\pi}}
          \int_{\mathbb R}s^2e^{-2as^2}\,ds+O(N^{-1/2})\\
   &=a+O(N^{-1/2}).
 \end{split}                                                    \tag{20}
\]
Outside the fixed neighborhood, the possible factors \(d_j^{-1}\)
cost at most a polynomial in \(N\), so their contribution
is exponentially smaller. The cyclic wrap term is
\(|g_D-g_0|^2=|N^2-1|^2\), also negligible compared with
\(\|g\|_2^2/N\). Thus
\(\|\mathsf S_Nu_N-u_N\|_2=\sqrt{a/N}+O(N^{-1})\).
Finally
\[
 \|(\mathsf S_N-I)(v_N-u_N)\|_2
                         \le2\|v_N-u_N\|_2=O(N^{-1})
 \tag{21}
\]
proves (17). \(\square\)

The proof is different from inferring a constant Fourier component
from a small shift residual. A pure nonconstant Fourier mode of
frequency one has residual \(2\sin(\pi/N)\) and exactly zero
constant component. Here positivity of \(g\), its explicit
Gaussian transform, and the controlled actual-source error
supply the lower bound. The general Fourier projection/current
identities already appear in
[the original Fourier-current calculation](actual_fourier_source_cancellation.md).
The new estimates above concern the prepared original
three-crossing vector with its fixed phase and norm.

For this actual vector the invariant projection itself has norm
asymptotic to \((2/\sqrt3)^{1/4}N^{-1/4}\), and therefore tends
to zero. Almost invariance is spread over a window of order
\(\sqrt N\) Fourier modes; it is not a uniform positive mass in
the invariant line. The source theorem supplies a polynomial
overlap bound despite that vanishing projection.

## 4. The unitary operator and the original test row

Define
\[
 \mathsf U_N=\mathsf D_N\mathsf S_N\mathsf D_N^{-1},
 \qquad
 a_N=\frac{\kappa^{-3}\omega_N^{-1}\alpha}{\|\alpha\|_2}.
 \tag{22}
\]
This is an explicit unitary representation of the cyclic group:
\(\mathsf U_N^N=I\), and
\[
 \|\mathsf U_Na_N-a_N\|_2
                     =\sqrt{\pi\sqrt3/N}+O(N^{-1}).
 \tag{23}
\]
Its original-coordinate entries include the parity-dependent wrap:
\[
 (\mathsf U_N f)_j=q^{2j+1}f_{j-1}\quad(1\le j<N),
 \qquad
 (\mathsf U_N f)_0=(-1)^Nq f_D.
 \tag{24}
\]
The invariant unit vector is
\(\mathsf D_N\mathbf1/\sqrt N\); its overlap with \(a_N\)
is exactly \(\widehat v_N(0)\).
More generally the normalized original test vectors
\[
 t_{N,m,j}=N^{-1/2}q^{j(j+2)}e^{2\pi imj/N}
 \tag{25}
\]
obey
\[
 \langle t_{N,m},\alpha\rangle
                            =\kappa^3\widehat\beta(m).
 \tag{26}
\]
Thus (16) is a lower bound for a specified linear functional
of the actual source, including its carrier phase.
No factorial change of norm is hidden in (22)--(26).

The literal quarter turn \(Jf_j=f_{D-j}\) is also explicit.
It satisfies
\[
 \mathsf D_N^{-1}J\mathsf D_N
                   =(-1)^Nq^{-1}\mathsf X_N^{-1}J,
 \qquad \mathsf X_N=\operatorname{diag}(Q^j).
 \tag{27}
\]
In our Fourier convention,
\[
 \widehat{Jz}(m)=Q^m\widehat z(-m),\qquad
 \widehat{(\mathsf D_N^{-1}J\mathsf D_N)z}(m)
       =(-1)^Nq^{-1}Q^{m+1}\widehat z(-m-1).
 \tag{28}
\]
These formulas follow by the literal replacement
\(j\mapsto D-j\). They retain the endpoint-index phase.
The turn alone therefore reflects and shifts the controlled
Fourier window; it does not destroy it.

The next crossing multiplication is a different operation.
The original \(M_N^p\) is not the unitary \(\mathsf U_N\),
does not commute with this shift, and can amplify an
\(O(N^{-1})\) norm error exponentially. Neither (17) nor
(28) proves preservation under a further \(M_N^p\).
Nor is the ordinary closing row the test (25): it is
\(\mathbf e_D^T\), and the proved exact-source endpoint
formula gives
\[
                         |\alpha_D|=N^{3/2}(1+O(N^{-1})).
 \tag{29}
\]
This is polynomial even though the overlaps (26) in the
specified window have exponential rate \(2J_0\).
The Fourier lower bound consequently cannot be substituted
for the original knot closure without an additional
source-preserving identity.

For the negative three-crossing source, conjugate
\(M,q,Q,\kappa,\omega_N,\mathsf D_N\).
The positive envelope and all norm estimates are unchanged.
Using the same unsigned Fourier transform gives exactly
(15) for its normalized dechirped source and (16) with
\(\omega_N\) conjugated. This follows either from the proof
or from \(\widehat{\overline z}(m)=\overline{\widehat z(-m)}\).
In particular no parity or crossing sign has been excluded.

## 5. Original-source diagnostics

The focused checker is
[check_three_crossing_fourier_packet.py](../experiments/check_three_crossing_fourier_packet.py).
It computes positive columns by the original crossing matrix
and negative columns by triangular inverse solves, retaining
the original cap. Its exact comparisons concern the chirp,
the parity-dependent cyclic seam, and the literal Fourier
turn formulas. The
[140-digit result](../repro/results/research-three-crossing-fourier-packet.json)
contains 20 signed-level cases and 2,004 exact comparisons,
with maximum relative residual below \(2.704\cdot10^{-138}\).

The same record gives finite shift residuals, actual Fourier
overlaps, Gaussian comparison errors, and the original closing
coefficient. Those numerical ratios are diagnostics only;
none supplies a premise of the asymptotic proof. The script
and dependency hashes and the arithmetic-library version
are recorded. Reproduction:

    python experiments/check_three_crossing_fourier_packet.py --precision 140
