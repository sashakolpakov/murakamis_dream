# A positive Jacobi problem for the original charge data

Research note, 3 November 2026. Frozen manuscripts are unchanged.

The ordinary physical values of the original edge satisfy a positive
Jacobi equation. This note identifies its boundary forcing, its exact
Fourier image, and the observation that is still needed to recover a
volume asymptotic. The positivity belongs to the value equation.
The original trace also uses first normals, and its observation is
different from the endpoint observation of the positive Green function.

The Jacobi recurrence and its real quadratic form are existing results
from the [edge difference equation](research_edge_kernel_difference_and_endpoint_bound.md).
The additional statements here are the positive-real row ratios for
complex free color, the explicit Fourier boundary problem, and the
improved bounds when the free color stays a fixed distance to the left
of the Jacobi spectrum.

## 1. The original value solution in a complex half-plane

Let \(N\ge3\), \(\theta=\pi/N\), \(c_j=2\cos((2j+1)\theta)\),
and \(s_x=2\sin(x\theta)\). Use the original Newton kernel
\[
 K_N(z,w)=\sum_{\ell=0}^{N-1}e_\ell(z)e_\ell(w),
 \qquad F_j(w)=K_N(c_j,w),\qquad
 J=\lfloor(N-1)/2\rfloor.
 \tag{1}
\]
For \(0\le r<J\), put
\[
 A_r=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\qquad
 C_r=\frac{s_r^4}{s_{2r}s_{2r+1}},\qquad C_0=0.
 \tag{2}
\]
All these coefficients are finite; \(A_r>0\) and \(C_r>0\)
for \(r>0\). The original value recurrence is
\[
 A_rF_{r+1}=(c_0+A_r+C_r-w)F_r-C_rF_{r-1},
 \qquad F_0=1.
 \tag{3}
\]
The range \(r<J\) is important. At even levels the next row
coalesces with its reflection and requires a first normal;
we do not impose an artificial ordinary equation there.

**Proposition 1.** Suppose \(\Re w<c_0\), and let
\(\delta=c_0-\Re w>0\). Every \(F_j(w)\), \(0\le j\le J\),
is nonzero. Its consecutive ratios obey
\[
 \Re\frac{F_{r+1}(w)}{F_r(w)}
                  \ge1+\frac{\delta}{A_r}>1.
 \tag{4}
\]
Thus each ratio has a single-valued logarithm with imaginary
part in \((-\pi/2,\pi/2)\) on this half-plane.

*Proof.* The first ratio is \(1+(c_0-w)/A_0\). If
\(\rho_r=F_r/F_{r-1}\) has real part at least one, then
\(\Re(1/\rho_r)\le1\). Equation (3) gives
\[
 \rho_{r+1}=1+\frac{c_0-w}{A_r}
                  +\frac{C_r}{A_r}(1-\rho_r^{-1}),
 \tag{5}
\]
which proves the induction. \(\square\)

For real \(w<c_0\), (3) also has an exact positive transfer
form. If \(d_r=(c_0-w)/A_r\), \(q_r=C_r/A_r\), and
\(\Delta F_r=F_r-F_{r-1}\), then
\[
 \binom{F_{r+1}}{\Delta F_{r+1}}=
 \begin{pmatrix}1+d_r&q_r\\d_r&q_r\end{pmatrix}
 \binom{F_r}{\Delta F_r},\qquad
                         \binom{F_0}{\Delta F_0}=\binom{1}{0}.
 \tag{6}
\]
Here \(\Delta F_0=0\) is a bookkeeping convention, since
\(C_0=0\). After the first step both coordinates are
strictly positive. In particular the original endpoint
condition has a nonzero component in the positive growing
direction.

At complete free color \(w=-2\), the limiting transfer
matrix at \(x=r/N\in(0,1/2)\) has eigenvalues
\[
 \lambda_+(x)=\cot^2(\pi x/2),\qquad
 \lambda_-(x)=\tan^2(\pi x/2).
 \tag{7}
\]
Indeed \(A_r,C_r\to\tan^2(\pi x)\), and its characteristic
polynomial is
\(\lambda^2-(2+4\cot^2(\pi x))\lambda+1\).
The two analytic roots remain strictly ordered in modulus
throughout \(0<\Re x<1/2\), because
\[
 |\cot(\pi x/2)|>1\quad\Longleftrightarrow\quad
                                      \cos(\pi\Re x)>0.
 \tag{8}
\]
This is a statement about the frozen value transfer.
It is not an interpolation theorem for the full finite
kernel away from the physical rows.

## 2. The forced positive boundary problem

Set
\[
 \pi_r=\frac{s_{2r+1}}{s_1},\qquad
 \pi_{r+1}C_{r+1}=\pi_rA_r.
 \tag{9}
\]
For \(1\le j\le J\), let \(\mathcal J_j\) be the symmetric
\(j\)-row Jacobi matrix with diagonal \(c_0+A_r+C_r\)
and off-diagonal \(-\sqrt{A_rC_{r+1}}\).
Its existing quadratic-form proof gives
\(\mathcal J_j>c_0I\), and in fact
\(\mathcal J_j-c_0I\ge16N^{-5}I\).
Consequently
\[
 \Re\langle h,(\mathcal J_j-wI)h\rangle
       \ge(\delta+16N^{-5})\|h\|^2,\qquad
 \|(\mathcal J_j-wI)^{-1}\|\le\delta^{-1}.
 \tag{10}
\]
The boundary condition of the original solution is explicit:
\[
 h_r=\sqrt{\pi_r}F_r(w),\quad
 (\mathcal J_j-wI)h
       =\sqrt{\pi_{j-1}}A_{j-1}F_j(w)e_{j-1},
 \qquad h_0=1.
 \tag{11}
\]
In particular
\[
 F_j(w)=
 \frac{1}{\sqrt{\pi_{j-1}}A_{j-1}
                  [(\mathcal J_j-wI)^{-1}]_{0,j-1}}.
 \tag{12}
\]
The denominator never vanishes in \(\Re w<c_0\). One can
see this either from (11) and Proposition 1 or directly
from the tridiagonal cofactor:
\[
 [(\mathcal J_j-wI)^{-1}]_{0,j-1}
       =\frac{\prod_{r=0}^{j-2}\sqrt{A_rC_{r+1}}}
                    {\det(\mathcal J_j-wI)}.
 \tag{13}
\]
For real \(w\le c_0\) it is strictly positive.
Equations (11)--(13) are an exact positive transmission
problem, with the original normalization \(F_0=1\).

The determinant identity also gives, for every integer
\(\ell\ge1\),
\[
 \left|\partial_w^\ell\log F_j(w)\right|
                \le(\ell-1)!\,j\,\delta^{-\ell}.
 \tag{14}
\]
Indeed \(F_j=\det(\mathcal J_j-wI)/\prod_{r<j}A_r\);
all eigenvalues of \(\mathcal J_j\) lie to the right of
the specified half-plane.

## 3. Its exact finite Fourier image

Fix an integer crossing power \(n\). Write
\[
 r_a=R(c_a)^n,\qquad |r_a|=1,\qquad
 \tau_a=\pi-(2a+1)\theta .
 \tag{15}
\]
The modulus statement concerns physical crossing values
only; no first normal is removed. On the first \(j\)
ordinary rows let \(D_n=\operatorname{diag}(r_a)\).
Then \(y=D_nh\) satisfies
\[
 H_n(w)y=
 \sqrt{\pi_{j-1}}A_{j-1}F_j(w)r_{j-1}e_{j-1},
 \qquad
 H_n(w)=D_n(\mathcal J_j-wI)D_n^* .
 \tag{16}
\]
It has the same accretivity and inverse bound (10).

Define an isometry \(U:\mathbb C^j\to\mathbb C^N\) by
\[
 (Ue_a)_k=\frac{e^{-ik\tau_a}-e^{ik\tau_a}}{\sqrt{2N}},
       \qquad 0\le k<N,\quad0\le a<j.
 \tag{17}
\]
The positive angles used here and their negatives are
distinct points of the original Fourier grid, so its
columns are orthonormal. Put
\[
 W=\operatorname{diag}\left(\frac{\sin\tau_a}{\sqrt{\pi_a}}\right)
      =\operatorname{diag}\sqrt{\sin\theta\sin\tau_a}.
 \tag{18}
\]
For the original source \(f=R^nK_N(\,\cdot\,,w)\), let
\(Z_k=\phi_N(fT_k(-z/2))\) and
\(\Delta_k=Z_{k+N}-(-1)^{N-1}Z_k\).
The exact derivative-sampling identity gives
\[
 UU^*\Delta=-iN\sqrt{2N}\,UWy .
 \tag{19}
\]
Thus the actual projected period increment satisfies
the finite matrix equation obtained from (16) by the
similarity \(UW\). On \(\operatorname{range}U\), its
operator and positive metric are
\[
 B=UWH_n(w)W^{-1}U^*,\qquad
                         G=UW^{-2}U^*.
 \tag{20}
\]
For \(z=UWy\),
\[
 \Re\langle z,GBz\rangle
     \ge\delta\langle z,Gz\rangle,\qquad
 \|B^{-1}\|\le\frac{\sqrt{N/2}}{\delta}.
 \tag{21}
\]
Here \(\operatorname{cond}(W)\le(\sin\theta)^{-1/2}
\le\sqrt{N/2}\); the metric has condition number at
most \(N/2\).
The right side of the equation for \(UU^*\Delta\) is
exactly
\[
 -iN\sqrt{2N}\sqrt{\pi_{j-1}}A_{j-1}
       F_j(w)r_{j-1}\,UW e_{j-1}.
 \tag{22}
\]
This is the original endpoint forcing, with its crossing
phase. It has not been replaced by a positive forcing
chosen for the Fourier problem.

At \(j=J\), the parity bookkeeping is simple. For odd
\(N\), every double node is included in (19); the omitted
simple node has \(\sin\tau_J=0\) and contributes no
period increment. Its value follows from the last row
of (3). For even \(N\), one double node remains outside
the truncation, namely \(a=J\). Its increment lies in
the orthogonal Fourier column \(Ue_J\) and is determined
by the boundary value \(r_JF_J\). Thus (19) is an exact
projection of the original full increment at both parities.

## 4. The first-normal terms and the remaining observation

For the double-node range
\(0\le j\le\lfloor(N-2)/2\rfloor\), let
\(G_j(w)=\partial_zK_N(c_j,w)\),
\(u_j=G_j/F_j\), \(Q(w)=G_0(w)\), and
\(P_N(w)=2T_N(w/2)+2\). The existing
[normal formula](research_physical_normal_lift.md#1-the-relative-normal-formula-already-proved)
is holomorphic on \(\Re w<c_0\):
\[
 \begin{split}
 c'(j)u_j={}&c'(0)Q+
   \operatorname{Tr}((\mathcal J_j-wI)^{-1}\mathcal J_j')
           -\sum_{r<j}A'(r)/A(r)\\
 &+\frac{c'(0)P_N(w)}{N^2s_1^2}
                    [(\mathcal J_j-wI)^{-1}]_{00},
 \qquad c'(j)=-4\theta\sin((2j+1)\theta).
 \end{split}
 \tag{23}
\]
The existing bounds
\(\|\mathcal J_j'\|\le6\pi N^3\),
\(|c'(j)|\ge8\pi/N^2\),
\(|A'/A|\le4\pi\), and \(j\le N/2\), together with
(10), imply
\[
 |u_j(w)|
 \le |Q(w)|+\frac{3N^6}{8\delta}
                +\frac{N^3}{4}+\frac{|P_N(w)|}{16\delta}.
 \tag{24}
\]
At \(j=0\), \(u_0=Q\). The two endpoint polynomials in
(24) remain explicit. They need not be polynomially
bounded on a fixed complex region.

The [geometric half-plane theorem](research_geometric_spectral_half_plane.md)
proves \(\Re w<7/4\) throughout the positive integer
path charge cube in its stated scope. Therefore \(N\ge16\) gives
\[
 c_0-\Re w>1/4-\pi^2/N^2>1/5.
 \tag{25}
\]
Thus the resolvent in this entire region is bounded by
\(5\), independently of \(N\) and the row count.
The \(Q\)- and \(P_N\)-free part of (24) is bounded by
\(15N^6/8+N^3/4\), and the explicit \(P_N\) term has
coefficient at most \(5/16\).

Finally the original central observation is
\[
 Z_0=(-1)^{N-1}
       \sum_{\text{double }j}r_jF_j
           \bigl\{(4-c_j^2)u_j-c_j+in b_j\bigr\}
       +\mathbf1_{N\ {\rm odd}}r_JF_J,\qquad
 b_j=\frac{N\tau_j\sin\tau_j}{\pi}.
 \tag{26}
\]
This formula retains the original normal at every double
node. Its row vector is different from the boundary
vector in (22). Therefore the positive Green entry in
(12), and the coercive Fourier problem (21), do not by
themselves give a lower bound for (26). They supply an
exact positive boundary problem with a known nonzero
physical transmission. The remaining question is the
overlap with the particular normal-weighted Fourier
observation (26).

## 5. Removing the endpoint growth inside a subsequent trace

There is a source-preserving way to replace the two explicit
endpoint terms in (23) when the free color \(w\) is subsequently
contracted by the original trace. It does not assert equality
of the off-grid functions.

Let \(\Pi_0\) be the full spectral idempotent at \(c_0\).
The [endpoint-normal identity](research_endpoint_normal_cap_rate.md#1-the-endpoint-derivative-as-an-actual-coupon)
is
\[
             Q(w)=\frac{\eta(T\Pi_0)(w)+c_0}{s_1^2},
                  \qquad\eta=(-1)^{N-1}.
 \tag{27}
\]
Let \(V_N(t)\) be the even logarithmic-factorial representative
of \(T\Pi_0\) from
[the odd Ward interpolation](research_odd_ward_logarithmic_factorial.md).
It is holomorphic on \(|\Re t|<\pi+\pi/N\), has all the
original value and first-normal data of
\((T\Pi_0)(-2\cos t)\), and satisfies
\[
 \sup_{|\Re t|\le\pi,\ |\Im t|\le H}|V_N(t)|
                       \le C_H(1+\log N).
 \tag{28}
\]
Define \(w(t)=-2\cos t\),
\(\widetilde Q_N(t)=(\eta V_N(t)+c_0)/s_1^2\).
For every physical double row \(j\ge1\), set
\[
 \widetilde u_j(t)=
 \frac{c'(0)}{c'(j)}\widetilde Q_N(t)
 +\frac{\operatorname{Tr}((\mathcal J_j-w(t)I)^{-1}
                                      \mathcal J_j')
               -\sum_{r<j}A'(r)/A(r)}{c'(j)}.
 \tag{29}
\]
Set \(\widetilde u_0=\widetilde Q_N\).

**Theorem 2.** At every physical free-color node, the
function \(F_j(w(t))\widetilde u_j(t)\) has the value and
every required first \(w\)-normal of \(G_j(w)\).
In particular it preserves the mixed first normal
\(\partial_z\partial_wK_N(c_j,w)\) at double free-color
nodes. The substitution is
exact inside a subsequent original trace in \(w\), with
arbitrary polynomial spectators. Products of these
substitutions preserve all mixed first normals used by
further original contractions.

On a fixed-height physical rectangle where
\(\Re w(t)\le c_0-\delta\), one has, uniformly in the
physical double row,
\[
 |\widetilde u_j(t)|
 \le C_H N^2(1+\log N)+\frac{3N^6}{8\delta}
                                      +\frac{N^3}{4}.
 \tag{30}
\]
For the geometric colors covered by (25), this is
\(O(N^6+N^2\log N)\), with a constant independent of
the path and its powers. Every fixed angle derivative
has the same polynomial type on interior compact
charts with a fixed half-plane margin.

*Proof.* Equation (27) and the full Ward interpolation
show that \(\widetilde Q_N\) has the full physical data
of \(Q\), not just its values. At every double free-color
root, \(P_N=P_N'=0\); at the odd simple root only
\(P_N=0\) is required. The resolvent in (23) is analytic
at all those nodes, because its spectrum lies strictly
above \(c_0\). Hence the omitted \(P_N\)-term has zero
required data. This proves the equality for \(u_j\).
Multiplication by the nonvanishing physical value
polynomial \(F_j\) proves the stated equality for \(G_j\).
The ordinary product rule proves the assertions with
spectators and mixed first normals.

Since \(s_1\ge4/N\), (28) gives
\(\widetilde Q_N=O_H(N^2(1+\log N))\).
The same resolvent estimate that proved (24) now gives
(30), with no \(P_N\)-term. On an interior compact chart,
one can enlarge the angle domain by a fixed amount
while retaining half the spectral margin. Cauchy's
formula proves the derivative estimates. At the odd
simple node \(t=0\), evenness makes the representative
holomorphic in \(w+2\); no extra normal is required.
\(\square\)

The theorem is a representative for a physical row
whose other endpoint is later traced. It supplies
polynomially bounded normal data at complex geometric
free color without estimating the canonical polynomials
\(Q\) and \(P_N\) there. It does not continue the row
index \(j\) to a second complex angle, and it does not
alter the scalar overlap problem in (26).

## 6. Finite reproduction

Run the focused check with

~~~sh
python3 experiments/check_physical_jacobi_charge_boundary.py \
  --precision 100 \
  --output repro/results/research-physical-jacobi-charge-boundary.json
~~~

The [script](../experiments/check_physical_jacobi_charge_boundary.py)
computes the physical rows and charge increments from the original
Newton matrices. It checks (4), (12), (16), and (19)--(22) at
levels \(3,\ldots,12\), with three complex free colors and powers
\(-3,0,3\), including both parity endpoints. The
[saved record](../repro/results/research-physical-jacobi-charge-boundary.json)
contains 90 source cases, 90 row-ratio comparisons, and 90
Green identities. It also compares the Ward-regularized formula
with 160 original kernel-normal values and 145 original mixed
first normals, including the odd simple endpoint values.
These finite comparisons check the normalizations;
the proofs above establish the statements at arbitrary level.
