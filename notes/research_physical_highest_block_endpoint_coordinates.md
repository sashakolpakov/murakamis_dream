# Physical highest-block coordinates for the whole intertwiner

Private written proof, 19 November 2026.

The physical highest block on one head is a pole-free coordinate on
the entire actual intertwiner space near the complete meridian.
Both endpoint columns and rows, and then every finite matrix block,
are recovered from that one remaining-head operator. Unlike the
constant coefficient after the prefix change of frame, this coordinate
does not require inverting a resonant remaining Cartan eigenvalue.

The seed is an arbitrary Cartan-preserving operator, not a scalar
vacuum value. Its freedom is essential. The theorem supplies an exact
finite reconstruction, a coupled low-degree norm envelope, whole-cap
bounds, and true meridian derivatives. It does not supply an analytic
phase or a nonzero closing coefficient for an unspecified seed.

The sole complete direct is C, pinned below. We use its finite prefix
operator and actual generator relations. All endpoint reconstruction,
nilpotence, terminal compatibility and estimates are proved here.

## 1. Actual heads and the endpoint coordinate

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
Keep \(q\) fixed and put \(M=e^\mu\), \(x=-M/q\). On one head,
\[
 Kw_a=xQ^{-a}w_a,\qquad
 Fw_a=(1-Q^{a+1})w_{a+1},\qquad
 Ew_a=e_aw_{a-1},\quad e_a=MQ^{-a}-M^{-1}.
 \tag{1}
\]
The lowering formula is used only for \(1\le a\le d\).
The outward arrows \(Ew_0,Fw_d\) are zero. In endpoint equations
below, \(e_0=e_N=0\) means these forced arrows, not evaluation of
the scalar expression in (1) at an omitted index.
Set \(f_a=\prod_{j=1}^a(1-Q^j)\), with \(f_0=1\).

There are \(m=r+1\) heads. Write \(U\) for the last \(r\) heads and
\(E,K,F\) for their ordered total generators; for \(r=0\) use
\(U=\mathbb C\), \(E=F=0\), \(K=1\). The total operators are
\[
 E_\Sigma=E_1K+E,\qquad
 F_\Sigma=F_1+K_1^{-1}F,\qquad K_\Sigma=K_1K.
 \tag{2}
\]
All products in (2) keep their tensor-head order. Let \(i_a:U\to
V_1\otimes U\) and \(p_a:V_1\otimes U\to U\) be the actual inclusion
and projection at first-head occupation \(a\). For an operator \(W\),
write \(W_{ab}=p_aWi_b\).

Define
\[
 \mathcal A_U=\{H\in\operatorname{End}(U):[K,H]=0\},\qquad
 \mathcal C_V=\{W:[E_\Sigma,W]=[F_\Sigma,W]=[K_\Sigma,W]=0\}.
 \tag{3}
\]
Since \(K(M)=M^rK(1)\), the vector space \(\mathcal A_U\) is independent
of \(M\). We also allow its exact integer-degree-preserving subspace;
integer degree is not identified modulo \(N\).

Whenever
\[
                         e_1e_2\cdots e_d\ne0,
 \tag{4}
\]
the map
\[
             \boxed{\quad\mathcal C_V\longrightarrow\mathcal A_U,
                    \qquad W\longmapsto H=W_{00}\quad}
 \tag{5}
\]
is a linear isomorphism. It is not asserted to preserve products.
Its inverse is holomorphic wherever (4) holds. In particular it is
holomorphic at \(M=1\), and throughout every scaled collar
\[
                 M=e^{u/N},\qquad |u|<\eta<\pi.
 \tag{6}
\]
The same assertion holds with exact integer-degree preservation
imposed on both sides. It applies to an actual physical braid
endomorphism with its end colors matched; its literal crossing and
framing scalars remain part of \(W\) and therefore of \(H\).

## 2. The finite endpoint equations

Taking first-head blocks of the two intertwining equations gives
\[
 \boxed{\quad
 e_{a+1}K W_{a+1,b}
       =e_bW_{a,b-1}K-[E,W_{ab}],
 \quad}
 \tag{7}
\]
\[
 \boxed{\quad
 (1-Q^{b+1})W_{a,b+1}
  =(1-Q^a)W_{a-1,b}
       +x^{-1}(Q^aFW_{ab}-Q^bW_{ab}F).
 \quad}
 \tag{8}
\]
Use zero blocks outside \(0\le a,b\le d\). Equation (7) includes
the final \(a=d\) compatibility row; (8) includes the final \(b=d\)
compatibility row. No inverse is taken in either omitted row.
Cartan commutation says exactly
\[
                         KW_{ab}=Q^{a-b}W_{ab}K.
 \tag{9}
\]

In particular, the first column \(C_a=W_{a0}\) is obtained by
\[
 C_0=H,\qquad C_{a+1}=-e_{a+1}^{-1}K^{-1}[E,C_a]
                         \quad(0\le a<d).
 \tag{10}
\]
The first row can independently be computed by
\[
 W_{00}=H,\qquad
 W_{0,b+1}=\frac{x^{-1}}{1-Q^{b+1}}
                     (FW_{0b}-Q^bW_{0b}F).
 \tag{11}
\]
Thus both physical endpoint families are determined, with their
actual relative orders. They are not replaced by a common scalar.

There are useful closed finite formulas. Let \(L_E,R_E\) denote
left and right multiplication by \(E\), and similarly for \(F\).
They commute with each other when they act on opposite sides.
The relation \(EK^{-1}=QK^{-1}E\) gives
\[
 C_a=\frac{(-1)^aK^{-a}}{e_1\cdots e_a}
          \prod_{j=0}^{a-1}(Q^jL_E-R_E)H,
 \qquad
 W_{0b}=\frac{x^{-b}}{f_b}
          \prod_{j=0}^{b-1}(L_F-Q^jR_F)H.
 \tag{12}
\]
The \(K^{-a}\) in the first expression acts on the left, after
the displayed product. Formula (12) follows by induction from
(10)--(11), and retains the two distinct endpoint polarizations.

## 3. Existence and every terminal row

We first verify the nilpotence used to close the reconstruction.
The summands \(E_i\prod_{j>i}K_j\) of an ordered total \(E\)
pairwise \(Q\)-commute. The summands
\((\prod_{j<i}K_j^{-1})F_i\) of a total \(F\) pairwise
\(Q^{-1}\)-commute. At a primitive root the intermediate
\(N\)-th quantum binomial coefficients vanish: their numerator
contains \(1-Q^N\), and their denominators only contain
\(1-Q^j\), \(0<j<N\). Expanding first for an indeterminate
quantum parameter and then evaluating proves the finite identity.
Induction on the number of summands, and the forced head caps,
therefore give
\[
                 E_\Sigma^N=F_\Sigma^N=E^N=F^N=0.
 \tag{13}
\]
This is at fixed \(q_N\) for every meridian in question, with no
ordinary-color quantum-normal specialization.

Given any \(H\in\mathcal A_U\), construct \(C_a\) by (10), and
put \(V_H=\sum_{a=0}^di_aC_a:U\to V_1\otimes U\).
The weight relation \(KC_a=Q^aC_aK\) follows inductively.
Equation (10) gives
\[
             E_\Sigma V_H-V_HE=i_dR,
                       \qquad R=[E,C_d].
 \tag{14}
\]
The apparent last row vanishes automatically. Indeed telescope
the \(N\)-th powers in (13):
\[
 0=E_\Sigma^NV_H-V_HE^N
   =\sum_{j=0}^dE_\Sigma^j i_dR E^{d-j}.
 \tag{15}
\]
Apply \(p_0\). Fewer than \(d\) factors of \(E_\Sigma\) cannot
lower the first head from \(d\) to zero. For \(j=d\), every factor
must use its first-head lowering summand, whose product is
\((e_1\cdots e_d)K^d\). Thus
\[
                         (e_1\cdots e_d)K^dR=0.
 \tag{16}
\]
Condition (4) and invertibility of \(K\) imply \(R=0\).

C's exact finite prefix change of frame is
\[
 S=\sum_{j=0}^d\frac{(x^{-1}L_1F)^j}{f_j},\qquad
 S^{-1}=\sum_{j=0}^d
          \frac{(-1)^jQ^{j(j-1)/2}(x^{-1}L_1F)^j}{f_j},
 \quad L_1w_a=w_{a-1},\quad L_1w_0=0.
 \tag{17}
\]
It satisfies \(S^{-1}F_\Sigma S=F_1\), commutes with the total
Cartan, and \(Si_0=i_0\). Consequently
\[
                    Si_b=f_b^{-1}F_\Sigma^bi_0.
 \tag{18}
\]
Define a finite operator \(T_H\), and then \(W_H\), by
\[
 T_H i_b=f_b^{-1}F_\Sigma^bV_H\quad(0\le b\le d),
                  \qquad W_H=T_HS^{-1}.
 \tag{19}
\]
Equation (13) includes the top \(F\) row, so (19) commutes with
\(F_\Sigma\). Its weights give \([K_\Sigma,W_H]=0\), and its
physical first column is \(V_H\).
The actual root relation
\([E_\Sigma,F_\Sigma]=(q-q^{-1})(K_\Sigma-K_\Sigma^{-1})\)
then implies that \([E_\Sigma,W_H]\) commutes with \(F_\Sigma\).
By (14)--(16) it vanishes on \(i_0U\). The vectors in (18) span
the whole space, so it vanishes everywhere. This proves existence
and both terminal equations in (7)--(8).

Conversely (7) determines the first column of any intertwiner
from \(H\); commutation with \(F_\Sigma\) and (18) then determines
the whole operator by (19). This proves uniqueness and (5).
Each operation in (10),(17),(19) preserves the exact total integer
degree when \(H\) has degree zero, which proves the integer version.
Only \(e_1,\ldots,e_d\), \(f_1,\ldots,f_d\), and units \(K,x\)
are divided by. Their asserted nonvanishing proves holomorphicity.

## 4. Actual collar bounds and coupled low degrees

Give every occupation basis its standard Euclidean norm. Fix the
number of heads and \(0<\eta<\pi\). All constants below may depend
on those choices, but not on \(N\), \(u\), or the seed.
For \(|u|\le\eta\), (1) gives the exact expression
\[
 e_j=-2i e^{-\pi i j/N}
              \sin\big((\pi j+iu)/N\big).
 \tag{20}
\]
Since the real part of its sine argument lies strictly between
zero and \(\pi\), the elementary inequalities
\(|\sin(s+it)|\ge|\sin s|\) and
\(\sin s\ge(2/\pi)\min(s,\pi-s)\) yield
\[
 |e_j|\ge \frac{4(\pi-\eta)}{\pi}
                  \frac{\min(j,N-j)}{N},\qquad 1\le j<N.
 \tag{21}
\]
All \(e_j\) also have a uniform upper bound. The analogous bounds
for \(1-Q^j\), and an elementary factorial estimate, imply
\[
 e^{-cN}\le |e_1\cdots e_a|\le e^{cN},\qquad
 e^{-cN}\le |f_a|\le e^{cN}\quad(0\le a<N).
 \tag{22}
\]
These estimates control all prefix products, not just the full product.
For an explicit lower-bound argument, replace each factor by a
constant times \(\min(j,N-j)/N\), with that constant at most one.
Every partial product of these numbers is at least their full
product, and \(n!\ge(n/e)^n\) bounds the latter below by \(e^{-cN}\).

The actual fixed-width operators \(E,F,E_\Sigma,F_\Sigma,K^{\pm1}\)
have uniformly bounded norm on this collar. Moreover
\(\|K^{\pm a}\|\le e^{r\eta}\) for \(a\le d\).
Formula (12) therefore bounds every \(C_a\) by
\(e^{cN}\|H\|\). Formula (17) bounds \(S^{\pm1}\) by \(e^{cN}\).
Finally (19), (22), and the finite number of blocks give
\[
              \boxed{\qquad
                 \|H\|\le\|W_H\|\le e^{cN}\|H\|.
              \qquad}\tag{23}
\]
Polynomial factors in \(N\) have been absorbed into \(e^{cN}\).
In particular there is no estimate of the form \(N^{cN}\) hidden
in the reconstruction.

There is a more informative coupled endpoint estimate. Choose a
fixed \(0<\delta<1/2\). For \(a\le\delta N\), (21) gives
\[
                  \|W_{a0}\|\le\frac{(cN)^a}{a!}\|H\|.
 \tag{24}
\]
For \(a+b+1\le\delta N\), (8) gives, with a larger fixed \(c\),
\[
 (b+1)\|W_{a,b+1}\|
      \le c a\|W_{a-1,b}\|+cN\|W_{ab}\|.
 \tag{25}
\]
Here \(|1-Q^a|\le 2\pi a/N\), whereas
\(|1-Q^{b+1}|\ge4(b+1)/N\). The two \(F\) terms have bounded
coefficients, including the exact \(x^{-1}\).

For nonnegative formal variables \(s,t\), define
\[
 \mathcal M_N(s,t)=\frac1{1-cst}
       \exp\left(cN\left[t+\frac{s}{1-cst}\right]\right).
 \tag{26}
\]
It has nonnegative coefficients and satisfies
\[
 \partial_t\mathcal M_N
      =cs^2\partial_s\mathcal M_N+cs\mathcal M_N+cN\mathcal M_N,
             \qquad \mathcal M_N(s,0)=e^{cNs}.
 \tag{27}
\]
Equations (24)--(25), by induction on \(b\), show that
\[
 \|W_{ab}\|\le\|H\|[s^at^b]\mathcal M_N(s,t)
                         \quad(a+b\le\delta N).
 \tag{28}
\]
All terms used in this induction stay within the displayed low band.
Thus this is a coupled two-endpoint estimate, not two unrelated
one-sided bounds.

For the whole finite operator-valued endpoint polynomial in the
ordinary physical first-head coordinates
\(\mathcal W_H(s,t)=\sum_{a,b=0}^dW_{ab}s^at^b\), the remaining
cap is also controlled. Equation (23) gives, for \(0<\rho<1\),
\[
 \left\|\sum_{a+b>\delta N}W_{ab}s^at^b\right\|
     \le N^2e^{cN}\rho^{\lfloor\delta N\rfloor+1}\|H\|,
                    \qquad |s|,|t|\le\rho.
 \tag{29}
\]
After the fixed cap constant is known, shrinking \(\rho\) makes
(29) at most \(e^{-\gamma N}\|H\|\), for any prescribed fixed
\(\gamma>0\). The low part is bounded by
\(\mathcal M_N(|s|,|t|)\|H\|\). This pays the complete cap in an
actual endpoint norm estimate; it does not turn an upper bound
relative to \(\|H\|\) into a lower bound for a scalar contraction.
An additional factorial or ordinary-binomial endpoint gauge changes
these coefficient bounds; its analytic effect is not included in
the envelope (26).

## 5. True meridian jets and the original closing

Let \(H(\mu)\) be holomorphic with values in the fixed space
\(\mathcal A_U\). Its extension in (19) is the literal fixed-
\(q_N\) meridian family. No quantum parameter is differentiated.
For \(0<\eta<\eta'<\pi\), Cauchy's formula and (23) imply, for
each fixed integer \(j\ge0\), provided the seed is holomorphic on
a neighborhood of the closed larger collar,
\[
 \sup_{|\mu|\le\eta/N}\|\partial_\mu^jW_H(\mu)\|
 \le j!\left(\frac{N}{\eta'-\eta}\right)^j e^{cN}
          \sup_{|\mu|\le\eta'/N}\|H(\mu)\|.
 \tag{30}
\]
The same argument differentiates (28)--(29) on smaller collars.
All first-head coefficients, tail coproducts, and changes of frame
are differentiated. For example differentiating (10) gives
\[
 e_aK\dot C_a=-[E,\dot C_{a-1}]-[\dot E,C_{a-1}]
                  -(\dot e_a+r e_a)KC_a,
       \qquad \dot e_a=MQ^{-a}+M^{-1}.
 \tag{31}
\]
Dots denote \(\partial_\mu\), and \(\dot K=rK\).
The omitted lowering arrows remain identically zero and therefore
have zero derivative. The full row normal is obtained by
differentiating (8), including \(\partial_\mu x^{-1}=-x^{-1}\)
and the actual \(\dot F\). Thus the root value and first normal
of both endpoint families are fixed by \(H(0),\dot H(0)\), with
no deleted resonance or terminal current.

The original highest-cut pivotal source is particularly direct
in these coordinates:
\[
 \boxed{\quad
 \Phi_0(W)=\operatorname{Tr}_{V_1\otimes U}
                ((P_0\otimes K^{1-N})W)
           =\operatorname{Tr}_U(K^{1-N}H).
 \quad}\tag{32}
\]
There is no new pivot on the opened head and no reset of a
transformed source. Its true first meridian derivative is
\[
 \dot\Phi_0(W)=\operatorname{Tr}_U
       \big(K^{1-N}\dot H+r(1-N)K^{1-N}H\big).
 \tag{33}
\]
Any separately prescribed exterior scalar multiplies (32), with
its own derivative in (33). Scalars already included in the actual
word remain in \(H\). No nonzero assertion about this finite trace
follows from (23), nor from invertibility of an actual word.

## 6. Exact composition and the remaining seed

The coordinate (5) has an explicit transported product. Define
\(U_a(H)=W_H{}_{0a}\) and \(V_a(H)=W_H{}_{a0}\) by (12). Then
\[
 \boxed{\qquad
 H_1\star H_2=\sum_{a=0}^d U_a(H_1)V_a(H_2),\qquad
                     W_{H_1\star H_2}=W_{H_1}W_{H_2}.
 \qquad}\tag{34}
\]
This is the literal first-head matrix multiplication, with no reset
of intermediate rows. It is associative by (5), has identity \(I_U\),
and retains all finite transfer indices. The original closing of a
product is therefore exactly
\[
 \Phi_0(W_{H_L}\cdots W_{H_1})
    =\tau(H_L\star\cdots\star H_1),\qquad
                  \tau(H)=\operatorname{Tr}_U(K^{1-N}H).
 \tag{35}
\]
Differentiating this finite product differentiates \(U_a,V_a\),
the seeds, and the pivot, as in (30)--(33). Formula (35) supplies
no positivity or nonvanishing for an invertible product.

For comparison only, C's transformed constant term is
\(B_0=p_0S^{-1}Wi_0\). The exact relation to the present seed is
\[
 B_0=\sum_{a=0}^d
      \frac{(-1)^aQ^{a(a-1)/2}x^{-a}}{f_a}\,F^aC_a.
 \tag{36}
\]
It is holomorphic at the complete point. Generically, where all
\(b_n=MKQ^{-n}-M^{-1}K^{-1}\) are invertible, C reconstructs
the whole operator from \(B_0\). Thus (36) is then an invertible
linear change between two copies of \(\mathcal A_U\): injectivity
follows from C's recursion and surjectivity from finite equal
dimensions and (5). The \(B_0\) chart is also multiplicative there,
because it is the constant coefficient of the \(F_1\)-Toeplitz
normal form. The physical \(H\) chart need not be multiplicative.
At \(M=1\), (36) can be singular, as C's explicit source coupon
shows; the physical chart (5) stays nonsingular.

This distinction addresses the actual endpoint reconstruction
problem but does not eliminate its seed. Every operator in
\(\mathcal A_U\) really is allowed by the homogeneous total
intertwiner equations. In particular those equations alone cannot
specify the remaining-head phase, its zeros, or its prescribed
pivotal trace. The physical \(H\) generally does not commute with
the remaining \(E,F\), so (5) cannot simply be iterated on \(H\)
to erase another head.

The initialized Gauss-type analytic propagation would additionally
need actual estimates for this coupled remaining-head seed, or a
separate source-specific identity fixing it. Equations (23)--(30)
are genuine finite transport bounds, but do not provide a uniform
analytic logarithm or a nonzero amplitude for an arbitrary seed.
No geometric relative-cycle coefficient, full angular-period lower
bound, or finite-exception conclusion is inferred.

## Complete direct-source pin

* C: notes/research_prefix_commutant_and_pointed_normal_functional.md,
  SHA256 b4fb801a1482316aebb4799f1d0b80d5b43ced39138d903c04cfde811ca166b0.

The complete direct was freshly read nontruncated in this active
author sequence. All used implications and source orders were checked.
Only written mathematics and text/hash operations were used; frozen
and public files were unchanged.
