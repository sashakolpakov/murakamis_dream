# Fixed-meridian growth of the canonical cutoff jump

Private written proof, 18 November 2026.

The actual quadratic reduction [Q] and the source connection [C]
give a nonzero fixed-meridian exponential rate on a suitable complex
quantum ray. The proof transports the original canonical cutoff jump,
including its exponentially small forcing. It does not assume a
projection onto a preferred solution or an ordering of complementary
characteristic roots.

## 1. Actual source, ray, and conclusion

Retain the simple Alexander node and actual cutoff source of [C].
Write
\[
 u=\log(Y/\alpha),\qquad
 D_R(h,u)=U_{R,+}(h,\alpha(e^u-1))
                         -U_{R,-}(h,\alpha(e^u-1)).
 \tag{1}
\]
The second argument of \(U\) is the displacement coordinate
\(z=Y-\alpha=\alpha(e^u-1)\) used in [C].
All endpoint sheets, cut, and framing are those
of [C]. Let \(\ell(u)\) be the other classical operator root through
one, and put
\[
 \kappa=\ell'(0)=-2\eta_*\alpha^2\ne0,\qquad
 \mathcal A(0)=0,\qquad \mathcal A'(u)=\log\ell(u),
 \tag{2}
\]
where \(\log\ell(0)=0\). Thus
\(\mathcal A(u)=\kappa u^2/2+O(u^3)\), and
\(\mathcal A(u)=S(\alpha e^u)\) in the notation of [C].

Choose a direction \(\theta\) with
\[
                        \Re(\kappa e^{i\theta})>0.
 \tag{3}
\]
Such a direction always exists. Choose the cutoff
\(R=\varrho e^{i\theta}\), with \(\varrho>0\) sufficiently small
for [Q]. Its construction permits this choice: its small-cutoff
conditions depend on \(|R|\), and the source sheets of [C] are
defined for every sufficiently small nonzero \(R\).
Take
\[
                    h=e^{i\theta}\varepsilon,\qquad
                    \varepsilon>0.
 \tag{4}
\]
This ray faces \(R\), and all functions and square-root choices in
[C] are fixed consistently on a surrounding closed facing subsector.

**Theorem.** There is \(T_0>0\) such that, for every fixed
\(0<T\le T_0\), the fixed meridian
\[
                  u_*=e^{i\theta}T,\qquad Y_*=\alpha e^{u_*}
 \tag{5}
\]
has the following property. For all sufficiently small positive
\(\varepsilon\), \(D_R(e^{i\theta}\varepsilon,u_*)\ne0\), and
\[
 \log|D_R(h,u_*)|
       =\Re\frac{\mathcal A(u_*)}{h}
                                  +O(\log(1/\varepsilon)).
 \tag{6}
\]
Equivalently, there are fixed \(C,M>0\) such that
\[
 C^{-1}\varepsilon^M
       e^{\Re(\mathcal A(u_*)/h)}
 \le |D_R(h,u_*)|
 \le C\varepsilon^{-M}
       e^{\Re(\mathcal A(u_*)/h)}.
 \tag{7}
\]
In particular
\[
 \lim_{\varepsilon\downarrow0}
       \varepsilon\log|D_R(e^{i\theta}\varepsilon,u_*)|
             =\Re(e^{-i\theta}\mathcal A(u_*))>0.
 \tag{8}
\]
The constants and the small-\(\varepsilon\) threshold may depend on
the chosen fixed \(T\). The target is reached exactly for every
sufficiently small \(\varepsilon\), not only on a subsequence.

This is a chosen-ray theorem for the actual canonical cutoff and
its operator branch. It is not a physical root-of-unity-ray theorem,
a statement about the original finite invariant, or an identification
with a hyperbolic representation component.

## 2. The quadratic equation and its roots

The complete source [Q] supplies one operator, common to the two
endpoint sheets and their difference,
\[
 \mathcal S_h=T^2+s_{1,h}(u)T+s_{0,h}(u),\qquad
 Tf(u)=f(u+h),
 \tag{9}
\]
on a fixed node disk. Its coefficients are holomorphic in \(u\),
uniformly bounded, and
\[
 s_{1,h}=-(1+\ell)+O(|h|),\qquad
 s_{0,h}=\ell+O(|h|).
 \tag{10}
\]
On a smaller fixed disk the actual source obeys
\[
 D_R(u+2h)+s_{1,h}(u)D_R(u+h)+s_{0,h}(u)D_R(u)
       =r_h(u),\qquad
 |r_h(u)|\le C_R e^{-\varrho/\varepsilon}.
 \tag{11}
\]
The reduction in [Q] removes the complementary factor on this
source, using its analytic type. No omitted-mode assumption is
introduced here. The coefficients need not be holomorphic in \(h\)
at zero; all estimates below are for each \(h\), uniformly as
\(\varepsilon\to0\).

Fix \(1/3<\beta<1/2\). On the ray \(u=e^{i\theta}t\), with
\(t\ge\varepsilon^\beta\), the two instantaneous roots of
\(\lambda^2+s_{1,h}\lambda+s_{0,h}\) have labels
\[
 \lambda_a(u)=1+O(\varepsilon/t),\qquad
 \lambda_g(u)=\ell(u)+O(\varepsilon/t).
 \tag{12}
\]
Their separation is comparable to \(t\).
To justify the labels, the discriminant is
\((\ell-1)^2+O(\varepsilon)\), and
\(|\ell-1|\asymp|u|\) on a sufficiently small punctured chart.
Since \(\varepsilon/t^2\to0\) uniformly on this part of the ray,
take the square root that is a small relative perturbation of
\(\ell-1\). This defines the two roots holomorphically on small
complex neighborhoods of the ray. Cauchy's estimate on disks of
radius a fixed multiple of \(t\) gives
\[
 \lambda_a'=O(\varepsilon/t^2),\qquad
 \lambda_g'=\ell'+O(\varepsilon/t^2).
 \tag{13}
\]
The coefficient \(O(\varepsilon)\) in (10) is available on a larger
fixed disk, so these Cauchy disks have the required bounds.

By (3), shrink \(T_0\) inside that fixed disk. Uniformly for
\(\varepsilon^\beta\le t\le T_0+O(\varepsilon)\),
\[
 |\lambda_g|\ge1+ct,\qquad
 \left|\frac{\lambda_a}{\lambda_g}\right|\le1-ct
 \tag{14}
\]
for some \(c>0\) and all sufficiently small \(\varepsilon\).
Indeed \(|\ell(e^{i\theta}t)|=1+\Re(\kappa e^{i\theta})t+O(t^2)\);
the errors \(\varepsilon/t=o(t)\) in (12) preserve the strict gap.

## 3. Exact grid and canonical initialization

For the chosen fixed \(T\), let
\[
 m_\varepsilon=
       \left\lfloor\frac{T-\varepsilon^\beta}{\varepsilon}\right\rfloor,
 \qquad
 t_0=T-m_\varepsilon\varepsilon,\qquad
 u_n=e^{i\theta}(t_0+n\varepsilon).
 \tag{15}
\]
For small \(\varepsilon\), this is a nonnegative integer, and
\[
 \varepsilon^\beta\le t_0<\varepsilon^\beta+\varepsilon,\qquad
                  u_{m_\varepsilon}=u_*.
 \tag{16}
\]
All shifted evaluations used in (11) stay in the fixed source disk
after the original choice of \(T_0\).

We need the ratio of the actual initial values, not an imposed
eigenvector. Choose \(\beta'\) with \(1/3<\beta'<\beta\).
The shrinking overlap of [C] says
\[
 D_R(h,u)=C_*h^{-1/2}e^{\mathcal A(u)/h}
                         E_h(u),\qquad
 C_*=2r\sqrt{-\eta_*}\sqrt\pi\ne0,
 \tag{17}
\]
where, on a complex disk of radius a fixed multiple of \(t_0\)
about \(u_0\),
\[
                    E_h(u)=1+O(\varepsilon^{3\beta'-1}).
 \tag{18}
\]
Indeed \(|\alpha(e^u-1)|\le C\varepsilon^\beta
<\varepsilon^{\beta'}\) there for small \(\varepsilon\), so this
disk lies inside the exact stated overlap of [C]. Its normalized
amplitude is holomorphic, and nonzero for small \(\varepsilon\).

Cauchy's estimate on nested such disks gives
\[
 \frac{E_h(u_0+h)}{E_h(u_0)}
       =1+O(\varepsilon^{3\beta'-\beta}).
 \tag{19}
\]
Taylor expansion of the fixed analytic action gives
\[
 q_0:=\frac{D_R(h,u_0+h)}{D_R(h,u_0)}
   =\ell(u_0)+O(\varepsilon)
                  +O(\varepsilon^{3\beta'-\beta})
   =\ell(u_0)+O(\varepsilon/t_0).
 \tag{20}
\]
Here \(3\beta'>1\), so the second amplitude error is
\(o(\varepsilon/t_0)\).

Introduce the instantaneous eigenframe
\[
 V_n=\begin{pmatrix}1&1\\
       \lambda_a(u_n)&\lambda_g(u_n)\end{pmatrix}.
 \tag{21}
\]
Write the actual initial vector as
\[
 \binom{D_R(h,u_0)}{D_R(h,u_0+h)}
                       =V_0\binom{a_0}{b_0}.
 \tag{22}
\]
By (12), (20), and the gap comparable to \(t_0\),
\[
 \rho_0:=\frac{a_0}{b_0}
       =\frac{\lambda_g(u_0)-q_0}{q_0-\lambda_a(u_0)}
       =O(\varepsilon/t_0^2).
 \tag{23}
\]
In particular \(b_0\ne0\), and (17) gives
\[
 b_0=C_*h^{-1/2}e^{\mathcal A(u_0)/h}(1+o(1)).
 \tag{24}
\]
The positivity in (3) implies
\(\Re(\mathcal A(u_0)/h)\ge c t_0^2/\varepsilon>0\)
for small \(\varepsilon\). In particular \(|b_0|\ge1\) eventually.
This last crude lower bound will suffice for the forcing estimate.

## 4. A growing cone for the homogeneous quadratic equation

First solve the homogeneous version of (11) with the actual two
initial values in (22). Denote this auxiliary solution by \(D^0_n\).
It is used only to estimate the actual forced solution.
The companion matrix is
\[
 C_n=\begin{pmatrix}0&1\\-s_{0,h}(u_n)&-s_{1,h}(u_n)\end{pmatrix},
 \qquad C_nV_n=V_n
                  \operatorname{diag}(\lambda_a(u_n),\lambda_g(u_n)).
 \tag{25}
\]
In moving coordinates \(X_n=(a_n,b_n)^t\), it follows that
\[
 X_{n+1}=M_n
       \operatorname{diag}(\lambda_a(u_n),\lambda_g(u_n))X_n,
 \qquad M_n=V_{n+1}^{-1}V_n=I+O(\varepsilon/t_n),
 \tag{26}
\]
where \(t_n=t_0+n\varepsilon\).
The estimate follows from (13), \(\|V_n\|\le C\), and
\(\|V_n^{-1}\|\le C/t_n\).

Whenever \(|\rho_n|=|a_n/b_n|\) is small, the exact fractional-linear
formula from (26), together with (14), gives
\[
 |\rho_{n+1}|
       \le(1-c_1t_n)|\rho_n|+C_1\varepsilon/t_n.
 \tag{27}
\]
The denominator is bounded away from zero. To see that the errors
in \(M_n\) preserve the displayed contraction, use
\(\varepsilon/t_n=o(t_n)\); decrease \(c_1\) if necessary.

Choose \(K\) larger than the initial constant in (23) and with
\(c_1K>2C_1\). The cone
\[
                       |\rho_n|\le K\varepsilon/t_n^2
 \tag{28}
\]
is invariant. Indeed (27) at the boundary saves
\((c_1K-C_1)\varepsilon/t_n\), whereas replacing \(t_n\) by
\(t_n+\varepsilon\) decreases the proposed boundary by at most
\(2K\varepsilon^2/t_n^3\). The latter is smaller because
\(\varepsilon/t_n^2\to0\), uniformly from \(t_0\) onward.
This also proves inductively that \(b_n\) never vanishes.

The second row of (26) consequently gives
\[
            b_{n+1}=\lambda_g(u_n)b_n
                               (1+O(\varepsilon/t_n)).
 \tag{29}
\]
The sum of these errors satisfies
\[
       \sum_{n=0}^{m_\varepsilon-1}\frac{\varepsilon}{t_n}
                                  =O(\log(1/\varepsilon)).
 \tag{30}
\]
Thus the homogeneous growing coefficient differs from
\(b_0\prod_{n<m_\varepsilon}\lambda_g(u_n)\) by a factor bounded
above and below by fixed powers of \(\varepsilon\).
Since \(D^0_n=a_n+b_n\), the same is true for \(D^0_n\);
the factor \(1+\rho_n\) stays away from zero.

## 5. The actual forcing cannot cancel this coefficient

In this section \(X_n\) denotes the moving-frame coordinates of the
actual source vector \((D_R(h,u_n),D_R(h,u_n+h))^t\), and \(X_n^0\)
denotes those of the homogeneous solution just estimated.
Write
\[
                 G_{p,q}=\prod_{n=p}^{q-1}|\lambda_g(u_n)|.
 \tag{31}
\]
For any subinterval, (14), (26), and (30) give the propagator bound
\[
 \left\|\prod_{n=p}^{q-1}
       M_n\operatorname{diag}(\lambda_a(u_n),\lambda_g(u_n))
       \right\|
                  \le C\varepsilon^{-M_1}G_{p,q}.
 \tag{32}
\]
The product is taken in its actual chronological order. This bound
does not assume that a vector already lies in the growing cone.

Subtract the homogeneous solution from the actual source vector.
The difference has zero initial vector and, at step \(n\), forcing
\[
                V_{n+1}^{-1}\binom0{r_h(u_n)}.
 \tag{33}
\]
Its norm is at most
\(C t_n^{-1}e^{-\varrho/\varepsilon}\).
Variation of constants, (32), and \(G_{0,n+1}\ge1\) from (14)
therefore give
\[
 \|X_{m_\varepsilon}-X^0_{m_\varepsilon}\|
       \le C\varepsilon^{-M_2}
             G_{0,m_\varepsilon}e^{-\varrho/\varepsilon}.
 \tag{34}
\]
For example, the sum of \(1/t_n\) is bounded by
\((m_\varepsilon+1)/t_0\), a fixed power of \(\varepsilon^{-1}\);
all such factors have been included in \(M_2\).

The homogeneous first coordinate has the lower bound
\[
            |D^0_{m_\varepsilon}|
                \ge C^{-1}\varepsilon^{M_3}
                         |b_0|G_{0,m_\varepsilon}.
 \tag{35}
\]
The bounded norm of \(V_{m_\varepsilon}\), (24), and
\(|b_0|\ge1\) show that the actual scalar error divided by (35)
tends to zero exponentially. Hence
\[
             D_R(h,u_*)=D^0_{m_\varepsilon}(1+o(1)),
 \tag{36}
\]
and it is nonzero for every sufficiently small \(\varepsilon\).
This step uses the actual initialized source and its actual residual;
it is not an assertion of invertibility alone.

## 6. Identification of the exponential rate

By (12), with the logarithm close to its classical branch,
\[
 \sum_{n<m_\varepsilon}
       \bigl(\log|\lambda_g(u_n)|-\log|\ell(u_n)|\bigr)
                                  =O(\log(1/\varepsilon)).
 \tag{37}
\]
The exact analytic action satisfies, at every step,
\[
 \frac{\mathcal A(u_n+h)-\mathcal A(u_n)}h
                    =\log\ell(u_n)+O(\varepsilon).
 \tag{38}
\]
There are \(O(\varepsilon^{-1})\) steps, so summation and taking
real parts give
\[
 \sum_{n<m_\varepsilon}\log|\ell(u_n)|
       =\Re\frac{\mathcal A(u_*)-\mathcal A(u_0)}h+O(1).
 \tag{39}
\]
Finally (24) says
\[
 \log|b_0|=\Re\frac{\mathcal A(u_0)}h
                         -\tfrac12\log\varepsilon+O(1).
 \tag{40}
\]
Equations (29)--(30), (36)--(40) prove (6)--(7).
The Taylor expansion in (2) and condition (3) make
\(\Re(e^{-i\theta}\mathcal A(e^{i\theta}T))>0\) for the chosen
small \(T_0\), proving (8).

The result is stronger than a norm bound: it retains the nonzero
canonical node coefficient, pays the moving eigenframe, controls
the actual additive forcing, and reaches a fixed target exactly.
It does not provide a convergent amplitude at that target, a full
moving Borel singularity theorem, or transport along arbitrary
meridian paths. In particular the chosen ray and operator component
are not identified with the physical root-of-unity ray or the
hyperbolic component. The arbitrary-short-filling volume problem,
including its cases with no Alexander-pole seed, remains open.

## 7. Complete proof sources

| Label | Complete source | SHA256 |
|---|---|---|
| Q | notes/research_canonical_cutoff_quadratic_ore_reduction.md | 90db0237f4536495e7150109eae374ebbb12e2f7515b7c577322d07d2b9daae7 |
| C | notes/research_canonical_cutoff_node_regularization_and_profile.md | 8c28a3d3a7b11085c8e2b5966221501b632ea99600aae4db57e8bdf8cd4a9631 |

Q supplies the actual quadratic quasiequation, its uniform coefficient
control and retained forcing. C supplies the canonical nonzero
shrinking overlap with its exact action and normalization. All root
estimates, initialization, cone transport, forcing comparison and
fixed-target rate estimates are proved above. Only written mathematics
and source-text reads were used. Frozen proofs and public manuscripts
are unchanged.
