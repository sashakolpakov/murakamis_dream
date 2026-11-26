# Compensated raising and the cap-observable endpoint current

Private written proof, 17 November 2026. A specified compensated
multiplication and shift descends to the minimal original cap
observation module. Together with its Jackson derivative it gives
a finite q-Weyl pair. Conjugation by the exact normal frame retains
a rank-one endpoint term. This constructs operators on that source
module; it does not identify an arbitrary neighboring coupon or turn.

## 1. The specified source and raising operator

Use the complete fixed-root conventions and original row of [M]:
\[
 N\ge3,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 \sigma=\pm1,\quad \tau=q^{2\sigma},\quad a=-q^\sigma,
 \qquad E_N=\mathcal B[c,y]/(c^N,y^N).
 \tag{1}
\]
Let \(D_c=D_{\tau,c}\), \(D_y=D_{\tau^{-1},y}\), and
\(\ell(F)=[t^d]F(at,t)\).
The minimal common kernel and its polynomial realization are
\[
 K_N=\bigcap_{r=0}^d\ker(\ell D_c^r),\qquad
 Q_N=E_N/K_N,\qquad
 \pi F(w)=\sum_{r=0}^d\frac{\ell D_c^rF}{[r]_\tau!}w^r.
 \tag{2}
\]
The independent probes and external parameters have exactly the
scope of [M]. In particular this quotient retains all restored
cap observations, rather than pointwise attachment values.
Write
\[
 S_yF(c,y)=F(c,\tau y),\qquad
 \mathcal R=\tau(c-ay)S_y
 \quad\hbox{on }E_N.
 \tag{3}
\]
Both operations preserve the defining ideal \((c^N,y^N)\).

**Exact descent.** Multiplication by \(w\), truncated modulo \(w^N\),
will be denoted by \(R\). Then
\[
 \pi\mathcal R=R\pi,\qquad \pi D_c=D_{\tau,w}\pi.
 \tag{4}
\]
Consequently \(\mathcal R\) preserves \(K_N\), even though
uncompensated multiplication need not preserve it.

Here is a proof with the endpoints retained. For \(0\le i,j<N\),
put \(k=d-j\). The explicit formula in [M] is
\[
 \pi(c^iy^j)=
 \mathbf1_{i+j\ge d}\,
 a^k{i\brack k}_\tau w^{i+j-d}.
 \tag{5}
\]
If \(i+j\le d-2\), both sides of (4) are zero. If \(i+j=d-1\),
the two terms of
\(\mathcal R(c^iy^j)=\tau^{j+1}
 (c^{i+1}y^j-a c^iy^{j+1})\)
have equal constant images and cancel. In the remaining degrees
below the top corner, q-Pascal gives
\[
 {i+1\brack k}_\tau-{i\brack k-1}_\tau
       =\tau^k{i\brack k}_\tau.
 \tag{6}
\]
The factor on the right after applying \(\pi\mathcal R\) is
\(\tau^{j+1+k}=\tau^N=1\), proving (4).
For \(i=d\) the absent \(c^N\) term is correctly represented by
\({N\brack k}_\tau=0\), \(0<k<N\).
For \(j=d\), the absent \(y^N\) term corresponds to \(k-1=-1\).
At \(i=j=d\), both terms vanish in \(E_N\), as does
\(w\pi(c^dy^d)\) modulo \(w^N\).
Thus no endpoint is inferred by extending an interior recurrence.

## 2. The finite q-Weyl pair

On \(Q_N\simeq\mathcal B[w]_{\le d}\), write
\[
 D=D_{\tau,w},\qquad K=I+(\tau-1)RD.
 \tag{7}
\]
Directly on \(w^j\),
\[
 DR-\tau RD=I,\qquad D^N=R^N=0,\qquad
 Kw^j=\tau^jw^j,\quad K^N=I,\quad KR=\tau RK.
 \tag{8}
\]
The top-degree check is essential:
\(DRw^d=0\), while
\(-\tau RDw^d=-\tau[d]_\tau w^d=w^d\).
Every lower degree uses
\([j+1]_\tau-\tau[j]_\tau=1\).
The lowering operator is the original descended \(D_c\);
the raising operator is the explicit source operation (3).
No Hopf coproduct, magnetic-head action, or neighboring crossing
is being assigned to this pair.

## 3. Exact frame conjugation, including its endpoint

The finite frame of [M] and [I] is
\[
 G(s)=e_\tau(sD)=\sum_{k=0}^d\frac{s^kD^k}{[k]_\tau!},
 \qquad P=\frac{D^d}{[d]_\tau!}.
 \tag{9}
\]
It is invertible for every complex \(s\); no factorial has index \(N\).
The operator \(P\) is rank one:
\(Pf=[w^d]f\), considered as a constant polynomial.
Since \(PD=DP=0\), \(PG(s)^{\pm1}=G(s)^{\pm1}P=P\).

The exact conjugation identities are
\[
 \boxed{\quad
 G(s)RG(s)^{-1}=R+sK-s^NP,\qquad
 G(s)KG(s)^{-1}=K\bigl(I+(\tau-1)sD\bigr).
 \quad} \tag{10}
\]
Indeed (8) gives by induction
\(D^kR=\tau^kRD^k+[k]_\tau D^{k-1}\).
Summing only through \(k=d\) yields
\[
 G(s)R=R G(\tau s)+sG(s)-s^NP.
 \tag{11}
\]
The finite identity
\(G(\tau s)=(I+(\tau-1)sD)G(s)\)
then proves the first part of (10). Either (7) or
\(DK=\tau KD\) proves its second part, with \(K\) on the left.

The endpoint term is forced by the central relation. If one
keeps only the apparent translation \(R+sK\), the root q-binomial
formula and \(KR=\tau RK\) give
\[
 (R+sK)^N=s^NI,
 \qquad
 \bigl(R+sK-s^NP\bigr)^N=0.
 \tag{12}
\]
For the first equality, every intermediate Gaussian binomial
coefficient at level \(N\) vanishes, and \(R^N=0,K^N=I\).
The second equality follows from the actual conjugation (10).
Thus the finite endpoint cannot be discarded in an exact operator
identity, even when its norm is very small.

For the full cap transport
\(U(s,t)=G(s)G(t)^{-1}\), put \(B_t=I+(\tau-1)tD\).
It has a finite nilpotent inverse. Exact composition of (10) gives
\[
 \boxed{\quad
 U(s,t)R U(s,t)^{-1}
   =R+(s-t)K B_t^{-1}+(t^N-s^N)P.
 \quad} \tag{13}
\]
To check the order, conjugation by \(G(t)^{-1}\) first gives
\(R-tK B_t^{-1}+t^NP\). Conjugating this by \(G(s)\)
replaces \(K\) by \(K B_s\), and
\(sB_t-tB_s=(s-t)I\).
In (13) \(K\) remains on the left.
Both endpoint powers are retained, and the formula becomes \(R\)
when \(s=t\). For the actual restored-cap frame in [M],
\(s=a\xi\) and \(t=\tau\zeta\).

## 4. Size, co-source, and exact scope

On the polynomial realization use the weighted coefficient norm
\(\|\sum f_jw^j\|_r=\sum|f_j|r^j\), \(r>0\).
Then the endpoint norm is exactly
\[
 \|s^NP\|_r=\frac{|s|^N}{r^d}
      =r\left(\frac{|s|}{r}\right)^N.
 \tag{14}
\]
For fixed \(r,C>0\) and \(|s|\le C/N\), this is at most
\(r(C/(Nr))^N\), and hence is smaller than every fixed exponential
rate as \(N\) grows. The two-endpoint term in (13) obeys the
corresponding sum bound.

The inherited quotient norm of [M] also gives an exact endpoint
bound. Its input monomial weights are \(r_c^ir_y^j\).
Formula (5) maps each total input degree to a different output
degree, so the quotient \(\ell^1\) norm splits over the \(w\)-degrees.
For the constant output all contributing coefficients have modulus
one, while the top output has only the input \(c^dy^d\). Hence
\[
 \|1\|_{Q_N}=\min(r_c,r_y)^d,\qquad
 \|w^d\|_{Q_N}=r_c^dr_y^d,\qquad
 \|s^NP\|_{Q_N}
       =\frac{|s|^N}{\max(r_c,r_y)^d}.
 \tag{14a}
\]
The first equality follows by concentrating the input on its
least weighted degree-\(d\) monomial; the triangle inequality
gives the reverse bound. Splitting by degree gives the stated
rank-one operator norm. Thus the endpoint is also
superexponentially small on the \(N^{-1}\) scale of the actual
quotient norm. No general uniform conditioning of \(\pi\) in
the polynomial-coordinate norm is asserted.

The prescribed cap row is still \(\lambda\operatorname{ev}_0\),
with the original \(\lambda=q^{\sigma d^2/2}\) retained. In particular
the first identity of (10) has the exact row consequence
\[
 \operatorname{ev}_0\bigl(G(s)RG(s)^{-1}f\bigr)
       =s f(0)-s^N[w^d]f.
 \tag{15}
\]
The original observation can see the endpoint. Smallness of the
operator term alone is not a relative estimate for this scalar,
whose other terms may cancel or vanish.

The previous rational-word local source system already retains
a q-exponential endpoint current on its rescaled original Newton
space. The new point here is the explicit operation (3) descending
through the common kernel of all restored cap observations, together
with (10)--(13) on that specified source module. It does not identify
the two representations or their crossing and turn actions.
An actual neighboring operator still requires an exact
kernel-preservation and source comparison. The terminal
homogeneous source in [M] remains \(\gamma_N\,1\), with
\(\gamma_N\) possibly zero; no nonzero geometric coefficient or
short-component lower bound follows from this q-Weyl realization.

## Complete direct sources

Both complete texts and their used implications were read.
The rational-word note was read in full for coverage, not used
to identify its original operators with (3).
Only written algebra was used.

| Label | Source | SHA-256 |
|---|---|---|
| I | [Invertible cap normal translation](research_invertible_cap_normal_translation.md) | 8f53a0d2a0c2a0009310392c88bfd0c4cdd82a089a82fbf567f6b7a4a7cff2d2 |
| M | [Minimal restored-cap observation module](research_minimal_restored_cap_normal_module.md) | bf59e93e40c9e42baf34e19a504326909df6d15f57ab086845e7e969df1c88e0 |
