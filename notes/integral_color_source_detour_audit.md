# The integral-color path: actual sources, pivots and dense resonances

Independent proof audit, 27 October 2026. The path
\(q_\lambda=e^{\pi i\lambda/N}\), \(M=-q_\lambda^N\) does give
an honest \(N\)-dimensional integral-color quotient and its actual
crossings. It is not automatically the same off-root source as
the auxiliary finite ADO lift with its root pivot frozen.
This distinction is explicit below.

The ordinary-color bounds impose a second exact constraint:
the actual color path has polynomial values on a sampling grid
of spacing \(O(1/N)\), and its nearest higher-root value is
literally one. A uniform positive dominant WKB solution on the
real interval cannot describe this selected function.

## 1. Exact quotient and basis comparisons

On the common balanced Verma module,
\[
 \delta=1-Q^N,\qquad w=M Q^{-N}-M^{-1},\qquad Q=q^2.
\]
The choice \(M=-q^N\) has \(w=0\). The tail is invariant and the
finite head is the genuine integral quotient, with
\[
 K e_j=q^{N-1-2j}e_j,\quad
 \mathcal E e_j=q^{-N}(1-Q^{N-j})e_{j-1},\quad
 F e_j=(1-Q^{j+1})e_{j+1}.
                                                               \tag{1}
\]
The original finite crossing is its literal quotient crossing.
The word excursion adapter is proportional to \(\delta w\),
so it vanishes on this whole path, not merely at its root endpoint.

Let \(u_j\) be the ordinary highest-weight basis with
\(Fu_j=u_{j+1}\),
\(Eu_j=[j]_q[N-j]_q u_{j-1}\), and
\(\mathcal E=\rho^2E\).
Then
\[
 e_j=u_j/(Q;Q)_j                                  \tag{2}
\]
gives exactly (1). For every fixed \(N\), this gauge is invertible
on \(0<\lambda\le1\), including at \(q_N\); all factors have
index \(j<N\). It is singular at \(q=1\).
The balanced coupon \(e_{ij}=1/N\) becomes
\[
 e^{\rm ordinary}_{ij}
     =\frac{(Q;Q)_j}{N(Q;Q)_i}.                  \tag{3}
\]
Its normalization remains one, but its separate source and
co-source flags need not have a regular \(q=1\) limit.

There is a second useful exact gauge, regular also at \(q=1\).
In the polynomial basis it gives
\[
 \mathcal E_{\rm sym}=v^{-1}(T_q-T_q^{-1}),\qquad
 F_{\rm sym}=v(q^nT_q^{-1}-q^{-n}T_q),\quad n=N-1.
\]
The diagonal conjugation from (1) is
\[
 D_j=(-1)^j q^{j(j+1)/2-Nj}{N-1\brack j}_{Q}.     \tag{4}
\]
Its adjacent ratio is the old \(\mathcal E\) coefficient divided
by \(q^j-q^{-j}\), which proves both generator comparisons.
At \(q=1\), \(D_j=(-1)^j\binom nj\); at the actual root,
\[
 D_j=q_N^{-Nj-j(j+1)/2},
\]
of modulus one. Thus (4) is invertible along the closed path for
fixed \(N\), but its condition number can be exponential in \(N\)
in the interior or at the classical endpoint. Exact finite
equivalence does not imply equality of naive principal symbols
in these different frames.

The normalized trace is basis invariant. On every one-cut
diagonal array, including the scalar index-weighted arrays,
the original balanced coupon equals this trace. This avoids
the coordinate singularity of (3) for those evaluations.
For off-diagonal Ward insertions the coupon must still be
transported; normalized trace is not a replacement on all matrices.

## 2. The pivotal adapter is essential off the root

The generic integral-color quantum invariant uses the ordinary
pivot \(g_{\rm int}=K\). The root ADO pivot is
\(g_{\rm root}=K^{1-N}\). Away from \(Q^N=1\),
\[
 S^2=\operatorname{Ad}K\ne\operatorname{Ad}K^{1-N}.
\]
For example their conjugations of \(\mathcal E\) differ by
\(Q^{-N}\). Hence a frozen ADO right cap is not a generic
Hopf pivotal cap, even though the quotient module and its
crossings are genuine.

For a \(b\)-strand knot braid of writhe \(\mathfrak w\), the
ordinary integral twist and frozen ADO twist at \(\alpha=n\) are
\[
 \theta_{\rm int}=q^{n(n+2)/2},\qquad
 \theta_{\rm root}=q^{-n^2/2}.
\]
Their ratio is \(q^{-Nn}\). The exact difference of the two
zero-framed state arrays is therefore the weight
\[
 q^{Nn(\mathfrak w-b+1)}
        (Q^N)^{\sum_{\text{closed strands}}j_a}. \tag{5}
\]
It retains an actual number-operator clock, not just a scalar.
At \(q_N\) its clock is one and its scalar is
\((-1)^{n(\mathfrak w-b+1)}=1\) by knot parity.
Thus the ordinary reduced endpoint is the original \(K_N\).
At \(q=1\), the ordinary reduced period is also one. Neither
endpoint equality removes the nonconstant adapter in between
or its quantum-normal derivatives.

There is an explicit small example. For \(N=2\), use the stabilized
unknot, the two-strand braid \(\sigma_1\). Its ordinary reduced
value is one. With the frozen pivot \(K^{-1}\) and frozen twist
\(q^{-1/2}\), its normalized one-cut value instead is
\[
 1+\frac{q^2-q^{-2}}2
       =1+i\sin(\pi\lambda).                    \tag{6}
\]
To check this, use the actual fundamental checked crossing
\(q^{1/2}I-q^{-1/2}U\), with
\(U|_{01,10}=\left[\begin{smallmatrix}q&-1\\-1&q^{-1}\end{smallmatrix}\right]\).
Closing the second leg with \(K^{-1}\), then applying the
frozen twist correction, gives diagonal entries
\(1\) and \(1-q^{-2}+q^2\); their average is (6).
It agrees at both endpoints but is not the integral-color
invariant inside the interval.

This is a comparison of two explicit interpolations, not a
claim that a generic ADO invariant was defined incorrectly.
The valid actual interpolation is \(C_N(q)\) with its ordinary
caps and twist. At the root its reduced one-cut evaluation is
regular even though its ordinary quantum dimension \([N]_{q_N}\)
vanishes. One must not evaluate an unreduced closure divided
by \([N]\) as two separately vanishing quantities.

## 3. Exact sampling and the necessary nonuniformity

Set
\[
 A_N(\lambda)=C_N(e^{\pi i\lambda/N}).
\]
For every integer \(r>N\), the value at
\(\lambda=N/r\) is an ordinary color at the principal root \(q_r\).
The actual unitary trace bound gives
\[
 |A_N(N/r)|\le [N]_{q_r}^{b-1}\le (r/2)^{b-1}.   \tag{7}
\]
On any fixed closed interval \(J\subset(0,1)\), these sampling
points have mesh \(O_J(1/N)\) and their bound is \(O_J(N^{b-1})\).

Consequently a positive dominant WKB expansion with a uniformly
nonvanishing subexponential amplitude cannot hold on any open
real interval below one. Choose a point of positive continuous
rate and a small compact interval on which it stays positive.
A sampling point in that interval contradicts (7).
More generally, if
\[
 u_N(\lambda)=N^{-1}\log^+|A_N(\lambda)|
\]
are equicontinuous on such a compact interval, then
\(\sup_Ju_N\to0\): compare every point with its neighboring
sampling point. Thus a positive exponential spike requires
loss of that equicontinuity.

There is an exact stronger endpoint ladder. At level \(r=N+k\),
ordinary-color Weyl symmetry gives
\[
 C_N(q_{N+k})=C_k(q_{N+k}),\qquad 1\le k<N.       \tag{8}
\]
For each fixed \(k\), the right side tends to one and is bounded.
In particular
\[
 A_N\!\left(\frac{N}{N+1}\right)=1              \tag{9}
\]
for every knot. Its distance from the target is \(1/(N+1)\).
If \(|K_N|\) has positive exponential rate, a nonzero smooth
dominant WKB amplitude cannot remain uniform even across this
endpoint window.

An unconditional quantitative form is
\[
 \sup_{\lambda\in[N/(N+1),1]}|A_N'(\lambda)|
       \ge (N+1)(|K_N|-1),
\]
and hence
\[
 \sup_{\lambda\in[N/(N+1),1]}
    |q\partial_q C_N(q)|
       \ge \frac{N(N+1)}\pi(|K_N|-1).            \tag{10}
\]
This follows by integrating the derivative along the interval,
so it does not assume a real-valued period or a mean-value point
for a complex function. The already proved figure-eight
asymptotic makes (9)--(10) an actual exponential endpoint
example. Ordinary-color unitarity controls values, not the
normal derivatives needed here.

Pointwise asymptotics at an individual nonsampled irrational
parameter are not excluded. Nor do these bounds exclude a
geometric branch with a resonance-dependent source coefficient.
They do exclude treating that coefficient as uniformly
nonzero and smooth merely because the classical optimizer is.

### A whole scaled boundary profile cannot be algebraic

The same exact ladder constrains the functions-before-jets program.
Use \(c=2\pi i\), \(H=\log Q\), and the scaled normal
\[
 z=N^2(H-c/N),\qquad
 \mathfrak f_N(z)=
     C_N\!\left(\exp\!\left[\frac{c}{2N}
                                  +\frac{z}{2N^2}\right]\right).
\]
The nearby principal level \(N+k\) is exactly
\[
 z_{N,k}=-\frac{ckN}{N+k}\longrightarrow-ck,\qquad
 \mathfrak f_N(z_{N,k})=C_k(q_{N+k})\longrightarrow1.     \tag{11}
\]
Also \(\mathfrak f_N(0)=K_N\).

Here is the precise conditional conclusion. Choose a subsequence
with \(|K_N|\to\infty\), for example one having a positive
exponential rate, and suppose
\(\mathfrak f_N/K_N\) converges locally uniformly to a holomorphic
function \(g\) on a connected domain containing zero and every
point \(-ck\), \(k\ge1\). Then
\[
 g(0)=1,\qquad g(-ck)=0\quad(k\ge1).             \tag{12}
\]
Local uniform convergence permits the moving evaluations (11),
so this needs no unproved interchange of pointwise limits.

Such a nonzero whole profile is not algebraic over \(\mathbb C(z)\).
Indeed, for an irreducible polynomial relation \(P(z,g)=0\),
the infinitely many zeros in (12) force \(P(z,0)\) to vanish
identically. Thus \(w\) divides \(P(z,w)\), forcing \(g=0\),
contrary to \(g(0)=1\).

Neither the required growth nor this normal-family convergence is
asserted for a general knot. A germ on a small neighborhood of
zero alone is not excluded, and the conclusion does not prohibit
algebraic coefficients for an individual local geometric WKB
branch. It says that, if a normalized whole selected boundary
profile exists through all nearby resonances, an algebraic
critical coefficient cannot be that entire profile. A genuinely
nonalgebraic period function is required; its resonance zeros and
one normalization do not determine it uniquely.

## 4. Principal flags depend on the valid source frame

The symmetric frame in (4) has principal functions
\[
 e=\frac{2\sinh(sT/2)}v,\quad
 f=2v\sinh(s(1-T)/2),\quad
 k=e^{s/2-sT},\qquad s=2\pi i\lambda.
\]
Its two eigenflags are
\[
 v_+=e^{s(1-T)/2}v,\qquad
 v_-=-e^{-sT/2}
       \frac{\sinh(s(1-T)/2)}{\sinh(sT/2)}v.
\]
The plus flag has degree \(+1\) and exactly the original
Fubini--Study current on the real sphere at every level
parameter. For \(0<\lambda<1\), the inverse flag has degree
\(-1\), whereas at \(\lambda=1\) its interior limit equals
the plus flag and has degree \(+1\).

Writing \(\varepsilon=1-\lambda\), the two inverse-flag bubbles are
\[
 v=\varepsilon y:\quad v_-\to-1/\bar y,\qquad
 V=1/v=\varepsilon y:\quad v_-\to\bar y .
\]
Each has degree \(-1\). Accordingly its signed weak current
has limit
\[
 \omega_{\rm FS}-\delta_{T=0}-\delta_{T=1}.
\]
For a direct check, the inverse-flag latitude tends to \(T\)
in the interior but has endpoint values \(1,0\); integration
by parts against the angularly averaged test function gives
exactly these two negative endpoint masses.

This verifies the current signs and shows why the earlier
ordinary-falling-frame plus bubble is not intrinsic. The
frame gauge can be nonuniform in \(N\). It does not permit
discarding the selected inverse eigenflag, the two genuine
endpoint bubbles in that frame, or the pivotal adapter (5).
No whole quantum dressing or selected norm follows from the
principal flag calculation alone.
