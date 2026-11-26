# The exact ordinary residual of a filled one-kernel leaf

Private written proof, 16 November 2026.

The literal filled-leaf polynomial has total bivariate degree \(N-1\).
This determines its ordinary difference-equation residual completely,
including the term invisible to the full physical algebra. Subtracting
the actual terminal source cancels that term. The same calculation
gives the original parameter derivative and an exact finite Chebyshev
ladder in the microscopic endpoint parameter. These are algebraic
source identities; no moderate-amplitude estimate is inferred.

## 1. Original source, symmetry and total degree

Use \(N\ge3\), and put
\[
 D=N-1,\qquad q=e^{\pi i/N},\qquad \eta=(-1)^D,\qquad
 \kappa=q^{D^2/2},\qquad c_j=q^{2j+1}+q^{-2j-1},
\]
\[
 s_j=2\sin(j\pi/N),\quad S_j=\prod_{\ell=1}^j s_\ell,\quad
 e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z),\quad
 P_N(Z)=2T_N(Z/2)+2 .
 \tag{1}
\]
Here \(S_0=1\), \(S_D=N\), and \(P_N\) is monic of degree \(N\).
The symbol \(T_N\) means Chebyshev's polynomial. The original
physical turn is \(T\), with \(Te_j=e_{D-j}\). Retain the full algebra
\[
 \mathcal A_N=\mathbb C[Z]/(P_N),\qquad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D},\qquad
 K_N(w,Z)=\sum_{j=0}^D e_j(w)e_j(Z).
 \tag{2}
\]
An algebra element is represented by its ordinary polynomial of
degree at most \(D\). All products involving the original crossing
\(R\) below take place in this full algebra before that representative
is taken. The endpoint \(w\) remains an ordinary complex variable.

For any signed integer \(n\), define the literal leaf
\[
 F_n(w,Z)=\big[T(R^nK_N(w,\cdot))\big](Z),\qquad
 c_{n,N}=\frac{\eta\kappa^n}{N^2}.
 \tag{3}
\]
Thus, with the original trace and every crossing carrier retained,
\[
 F_n(w,Z)=
 \phi_N^{(X)}\!\left[K_N(Z,X)R^n(X)K_N(w,X)\right].
 \tag{4}
\]
Indeed \((Tf)(Z)=\sum_i e_i(Z)\phi_N(e_i f)\).
Formula (4) proves the ordinary symmetry
\(F_n(w,Z)=F_n(Z,w)\).

**Proposition 1.** For every signed \(n\),
\[
 \deg_{\mathrm{total}}F_n=D,\qquad
 [w^D]F_n=[Z^D]F_n=c_{n,N}.
 \tag{5}
\]
Both displayed coefficients are independent of the other variable.

*Proof.* The terminal Newton spaces
\[
 I_j=\operatorname{span}\{e_j,\ldots,e_D\}
\]
are ideals, since
\(Ce_j=c_je_j-s_{j+1}^2e_{j+1}\) for canonical multiplication \(C\).
Multiplication by the unit \(R^n\) therefore preserves \(I_j\) for
every signed \(n\). Since \(TI_j\) consists of polynomials of degree
at most \(D-j\),
\[
 F_n(w,Z)=\sum_{j=0}^D e_j(w)\,[T(R^ne_j)](Z)
 \tag{6}
\]
has total degree at most \(D\). The original endpoint carrier is
\(R^ne_D=\kappa^ne_D\). The term \(j=D\) in (6) is consequently
\(\kappa^ne_D(w)\); all other terms have smaller \(w\)-degree.
As \([w^D]e_D=\eta/N^2\), its coefficient is \(c_{n,N}\ne0\).
Symmetry gives the same \(Z\)-coefficient and proves (5).
\(\square\)

Put
\[
 J=TCT,\qquad V_n=\kappa^nTR^{-n}T,\qquad
 D_n=V_nCV_{-n}.
 \tag{7}
\]
The original one-kernel equation is
\[
 (w-J)K_N(w,\cdot)=\frac{\eta P_N(w)}{N^2}e_D.
 \tag{8}
\]
Conjugation by \(TR^n\), using
\((TR^n)J(TR^n)^{-1}=D_{-n}\), gives the exact full-algebra identity
\[
 (w-D_{-n})F_n(w,\cdot)=c_{n,N}P_N(w)\,1.
 \tag{9}
\]
In particular (9) retains every double-root first normal and the
odd-level simple value. It does not by itself specify the ordinary
residual away from the physical spectrum.

## 2. The ordinary operator and its raising coefficient

Use the ordinary polynomial lift \(\widetilde J\) of the original
difference operator. In \(Z=v+v^{-1}\), let \(E\) replace \(v\) by
\(q^2v\), and set
\[
 A(v)=-\frac{(qv-1)^4}{q(v^2-1)(q^2v^2-1)},\qquad
 B(v)=A(v^{-1}),\qquad r(v)=\frac8{Z+c_0}.
\]
Then
\[
 \widetilde J=r(v)-A(v)E-B(v)E^{-1}.
 \tag{10}
\]
The apparent poles cancel on inversion-even Laurent polynomials,
giving ordinary polynomials in \(Z\). This is the ordinary lift
in the pinned operator sources, not a new interpolation. It preserves
the ideal \((P_N)\), since \(P_N(v+v^{-1})\) is unchanged by \(E\).

For \(\sigma=\pm1\), define
\[
 \widetilde D_0=\widetilde C,\qquad
 \widetilde D_\sigma=
 \frac8{c_0}I+
 \frac{q^{-\sigma}\widetilde J\widetilde C
             -q^\sigma\widetilde C\widetilde J}
      {q^{2\sigma}-q^{-2\sigma}},
 \tag{11}
\]
where \(\widetilde C\) is ordinary multiplication by \(Z\). For \(k\ge0\)
use the ordered recurrence
\[
 \widetilde D_{\sigma(k+2)}
 =8q^{-\sigma}I-q^{-2\sigma}\widetilde D_{\sigma k}
       -q^{-\sigma}\widetilde D_{\sigma(k+1)}\widetilde J.
 \tag{12}
\]
These operators preserve \((P_N)\) and descend to the canonical
\(D_n\) in (7). The order on the last product in (12) is part
of the definition. All denominators in (11) are nonzero for \(N\ge3\).

**Lemma 2.** For every ordinary polynomial degree \(d\ge0\),
\[
 \widetilde JZ^d=c_d Z^d+\text{terms of degree less than }d,
 \qquad
 c_d=q^{2d+1}+q^{-2d-1},
 \tag{13}
\]
and, for every signed integer \(n\),
\[
 \widetilde D_nZ^d
   =(-1)^nq^{-2n(d+1)}Z^{d+1}
        +\text{terms of degree at most }d .
 \tag{14}
\]
In particular every raising coefficient in (14) is nonzero.

*Proof.* As \(v\) tends to infinity,
\(A(v)\to-q\), \(B(v)\to-q^{-1}\), and \(r(v)=O(v^{-1})\).
Since \(\widetilde JZ^d\) is already an ordinary polynomial,
(10) proves its degree bound and the coefficient (13).
In (11) the coefficient of \(Z^{d+1}\) is
\[
 \frac{q^{-\sigma}c_{d+1}-q^\sigma c_d}
      {q^{2\sigma}-q^{-2\sigma}}
       =-q^{-2\sigma(d+1)}.
 \tag{15}
\]
Thus (14) holds at \(n=0,\sigma\).
The degree bound follows for all signed \(n\) by (12).
At a fixed \(d\), its raising coefficients obey
\[
 a_{\sigma(k+2)}
   =-q^{-2\sigma}a_{\sigma k}
       -q^{-\sigma}c_d a_{\sigma(k+1)}.
 \tag{16}
\]
The expression \(a_{\sigma k}=(-1)^kq^{-2\sigma k(d+1)}\)
has the two required initial values and satisfies (16):
the two roots of that scalar recurrence are
\(-q^{-2\sigma(d+1)}\) and \(-q^{2\sigma d}\).
This proves (14), including negative \(n\). \(\square\)

At the canonical top degree \(d=D\), \(q^{2(D+1)}=1\).
Hence the raising coefficient of \(\widetilde D_{-n}\)
on \(Z^D\) is exactly \((-1)^n\).

## 3. Exact ordinary residual and terminal subtraction

**Theorem 3.** The following is an identity of ordinary bivariate
polynomials for every complex \(w,Z\) and every signed integer \(n\):
\[
 \boxed{\quad
 (w-\widetilde D_{-n}^{\,Z})F_n(w,Z)
     =c_{n,N}\big[P_N(w)-(-1)^nP_N(Z)\big].
 \quad}
 \tag{17}
\]
The operator acts in the indicated variable. By symmetry there is
also the exact identity
\[
 (Z-\widetilde D_{-n}^{\,w})F_n(w,Z)
     =c_{n,N}\big[P_N(Z)-(-1)^nP_N(w)\big].
 \tag{18}
\]

*Proof.* The difference between the two sides of (9), calculated
with the ordinary lift, is divisible by \(P_N(Z)\). By (5) and
Lemma 2 its \(Z\)-degree is at most \(N\). Its coefficient of
\(Z^N\) is
\[
                 -(-1)^n[Z^D]F_n=-(-1)^nc_{n,N}.
 \tag{19}
\]
Since \(P_N\) is monic, this fixes the entire multiple and proves
(17). Equation (18) follows from (4). \(\square\)

The zero-power case provides an ordinary normalization check:
the pinned reproducer identity gives
\[
 F_0(w,Z)=TK_N(w,Z)
       =\frac{P_N(Z)-P_N(w)}{\eta N^2(Z-w)}.
 \tag{20}
\]
Multiplication by \(w-Z\) is exactly (17) at \(n=0\), including
the removable diagonal \(Z=w\).

Write the actual terminal and its actual parameter derivative as
\[
 G(Z)=F_n(c_0,Z)=T(R^n)(Z),\qquad
 H(Z)=\partial_wF_n(c_0,Z)=T(R^nQ_N)(Z),
\]
\[
 Q_N(Z)=\left.\partial_wK_N(w,Z)\right|_{w=c_0}.
 \tag{21}
\]
The notation agrees with \(G=G_{-n}\), \(H=H_{-n}\) in the
pinned terminal source. Since \(P_N(c_0)=P_N'(c_0)=0\),
(17) implies
\[
 (c_0-\widetilde D_{-n})G=-(-1)^nc_{n,N}P_N(Z).
 \tag{22}
\]
The terminal polynomial therefore has an explicit ordinary
residual even though its full physical eigen-equation is homogeneous.

Set \(\Delta_n(w,Z)=F_n(w,Z)-G(Z)\). Its top \(Z\)-coefficient
cancels, so \(\deg_Z\Delta_n\le D-1\), and subtraction gives
\[
 \boxed{\quad
 (w-\widetilde D_{-n})\Delta_n
       =c_{n,N}P_N(w)-(w-c_0)G.
 \quad}
 \tag{23}
\]
There is no \(P_N(Z)\) term in (23). For each \(w\), this is the
unique ordinary solution of degree at most \(D-1\). Indeed,
if a nonzero polynomial \(p\) has degree \(d\le D-1\), then
\((w-\widetilde D_{-n})p\) has degree \(d+1\) and nonzero leading
coefficient by (14); it cannot vanish.

Differentiating (17) in the ordinary parameter \(w\) yields,
for every integer \(k\ge1\),
\[
 (w-\widetilde D_{-n})\partial_w^kF_n
       +k\partial_w^{k-1}F_n=c_{n,N}P_N^{(k)}(w).
 \tag{24}
\]
Here \(\deg_Z\partial_w^kF_n\le D-k\) when \(k\le D\),
by total degree. For the microscopic parameter
\(w_N(\alpha)=2\cosh(\alpha/N)\), the first equation reads exactly
\[
 (w_N(\alpha)-\widetilde D_{-n})
       \partial_\alpha F_n(w_N(\alpha),Z)
 =2c_{n,N}\sinh\alpha
       -\frac2N\sinh(\alpha/N)F_n(w_N(\alpha),Z).
 \tag{24a}
\]
This entire identity uses no division by \(\sinh(\alpha/N)\).
At the original physical endpoint, (24) gives
\[
 \boxed{\qquad(\widetilde D_{-n}-c_0)H=G.\qquad}
 \tag{25}
\]
Equation (25) is an ordinary polynomial identity, not just a
canonical Jordan relation. It involves the derivative of the actual
endpoint parameter, not a derivative chosen from a scalar
interpolant of physical values.

## 4. The universal residual for an ordinary endpoint product

The same top-coefficient argument applies without a bivariate
total-degree assertion for products. For \(r\ge1\), put
\[
 B_r=\operatorname{can}\prod_{i=1}^r K_N(w_i,Z),\qquad
 F_{n,r}=T(R^nB_r),\qquad
 \lambda_r=\sum_{i=1}^r w_i-(r-1)c_0.
 \tag{25a}
\]
All endpoint parameters remain ordinary. Let \(M_r\) be precisely
the canonical mixed source of the original product equation:
\[
 (\lambda_r-J)B_r
       =\frac{\eta}{N^2}\left(\sum_iP_N(w_i)\right)e_D+M_r.
 \tag{25b}
\]
For clarity, this is the source obtained by the product rule in
the original ordinary difference operator. With
\(k_i(v)=K_N(w_i,v+v^{-1})\) and
\(\Delta_\pm k_i(v)=k_i(q^{\pm2}v)-k_i(v)\), its ordinary
representative before canonical reduction is
\[
 A(v)\!\sum_{\substack{I\subset\{1,\ldots,r\}\\|I|\ge2}}
      \prod_{i\in I}\Delta_+k_i\prod_{i\notin I}k_i
 +B(v)\!\sum_{\substack{I\subset\{1,\ldots,r\}\\|I|\ge2}}
      \prod_{i\in I}\Delta_-k_i\prod_{i\notin I}k_i .
 \tag{25c}
\]
The paired expression is an ordinary polynomial and gives the
same \(M_r\) as (25b), by the pinned source's exact product rule.
Set \(F_{n,0}=G\), \(\lambda_0=c_0\), \(M_0=M_1=0\).

**Corollary 3.1.** For every fixed number of factors, the exact
ordinary identity is
\[
 \boxed{\quad
 (\lambda_r-\widetilde D_{-n})F_{n,r}
  =c_{n,N}\sum_iP_N(w_i)+T(R^nM_r)
                 -(-1)^nc_{n,N}P_N(Z).
 \quad}
 \tag{25d}
\]
The term \(T(R^nM_r)\) is its original canonical polynomial,
including all shared endpoint parameters and all physical normals.

*Proof.* Every endpoint kernel has value one at \(c_0\);
therefore \(B_r(c_0)=1\). For every canonical polynomial \(a\),
\([e_0]a=a(c_0)\), and hence
\[
 [Z^D]Ta=\frac{\eta}{N^2}a(c_0).
 \tag{25e}
\]
Using \(R^n(c_0)=\kappa^n\) gives
\([Z^D]F_{n,r}=c_{n,N}\), independently of \(r\) and of
all endpoint parameters. Conjugating (25b) by \(TR^n\) proves
(25d) in the full quotient without its last term. The ordinary
residual has degree at most \(N\), and Lemma 2 fixes its leading
coefficient as \(-(-1)^nc_{n,N}\). It is a multiple of \(P_N\),
so it is exactly the last term displayed. \(\square\)

Specialize one endpoint, say \(w_r\), to \(c_0\) and write
\(F_{n,r-1}\), \(M_{r-1}\) for the resulting objects with that
factor removed. Formula (25c) shows this is literally the same
mixed source: all differences of \(K_N(c_0,Z)=1\) vanish.
Then
\[
 \deg_Z(F_{n,r}-F_{n,r-1})\le D-1
\]
and the exact ordinary endpoint-difference equation is
\[
 \boxed{\begin{split}
 (\lambda_r-\widetilde D_{-n})(F_{n,r}-F_{n,r-1})
   ={}&c_{n,N}P_N(w_r)
       +T\!\left(R^n(M_r-M_{r-1})\right)\\
     &-(w_r-c_0)F_{n,r-1}.
 \end{split}}
 \tag{25f}
\]
This solution is unique in degree at most \(D-1\), by Lemma 2.
The universal top residual is already present in the bare terminal
\(G\); every endpoint difference removes it. Equation (25f) retains
the transformed mixed forcing and makes no estimate of that term.

## 5. The exact parameter ladder and its frequency band

For this section \(D_{-n}\) denotes the canonical operator, and
\(U_\ell\) denotes Chebyshev's polynomial of the second kind,
normalized by \(U_{-1}=0,U_0=1\).
Set \(w_N(\alpha)=2\cosh(\alpha/N)\). Since \(F_n\) has degree
at most \(D\) in \(w\), it has the exact finite expansion
\[
 F_n(w_N(\alpha),Z)
       =\sum_{k=-D}^{D} A_{k,N}(Z)e^{k\alpha/N},
       \qquad A_{-k,N}=A_{k,N}.
 \tag{26}
\]

**Proposition 4.** Its coefficients are exactly
\[
 \boxed{\quad
 A_{k,N}=c_{n,N}
          U_{D-k}(D_{-n}/2)\,1,\qquad 0\le k\le D.
 \quad}
 \tag{27}
\]
They are ordinary canonical polynomials with
\[
 \deg_Z A_{k,N}=D-k,\qquad
 [Z^{D-k}]A_{k,N}
   =c_{n,N}(-1)^{n(D-k)}
                   q^{\,n(D-k)(D-k+1)}.
 \tag{28}
\]

*Proof.* Put \(z=e^{\alpha/N}\). The full-algebra equation (9) becomes
\[
 (z+z^{-1}-D_{-n})\sum_{k=-D}^{D}A_{k,N}z^k
       =c_{n,N}(z^N+z^{-N}+2).
 \tag{29}
\]
The coefficient of \(z^N\) is \(A_{D,N}=c_{n,N}1\).
Writing \(A_{N,N}=0\), the remaining positive coefficients give
\[
 A_{k-1,N}=D_{-n}A_{k,N}-A_{k+1,N},
                 \qquad 1\le k\le D .
 \tag{30}
\]
This proves (27). The middle coefficient is consistent exactly
because \(P_N(D_{-n})=0\), by conjugation of \(P_N(C)=0\):
\[
 2U_{N-2}(D_{-n}/2)
       -D_{-n}U_{N-1}(D_{-n}/2)
          =-2T_N(D_{-n}/2)=2I.
 \tag{31}
\]
No ordinary off-grid eigen-equation was used here.
For \(m=D-k\le D\), the leading term of \(U_m(D_{-n}/2)1\)
is that of \(D_{-n}^m1\). These successive raises never exceed
degree \(D\), so no canonical reduction changes them.
Multiplying the nonzero coefficients from (14) proves (28).
\(\square\)

Consequently the polynomial-valued entire family (26) has exact
exponential type \(D/N\), with respect to any fixed norm on the
finite-dimensional polynomial space at that level: its extreme
coefficient is the nonzero constant \(c_{n,N}\).

There is a sharper band statement for the raw physical normal
radical. Put
\[
 J_*=\left\lfloor\frac{N-1}{2}\right\rfloor,\qquad
 m=\left\lfloor\frac N2\right\rfloor,
\]
and let \(\mathcal L_N\) be ordinary interpolation of the values
at the \(J_*+1\) distinct physical colors, of degree at most \(J_*\).
Then
\[
 \mathcal R_n(\alpha,Z)
   =F_n(w_N(\alpha),Z)
          -\mathcal L_N\big[F_n(w_N(\alpha),\cdot)\big](Z)
 \tag{32}
\]
has zero physical values and retains the difference of the original
first normals. Since \(D-J_*=m\), (28) shows that
\[
 \mathcal R_n(\alpha,Z)
       =\sum_{|k|\le m-1}
           (I-\mathcal L_N)A_{k,N}(Z)e^{k\alpha/N}.
 \tag{33}
\]
The coefficient at \(k=m-1\) has degree
\(D-m+1=\lceil N/2\rceil>J_*\), so it is nonzero after the
interpolation subtraction. Thus its polynomial-valued type is
exactly \((m-1)/N<1/2\), including both parities.
This last exact type is for the polynomial-valued family;
its highest coefficient can vanish at a particular output color.

This raw radical is defined by the global value interpolant
\(\mathcal L_N\). It is not the normalized derivative mismatch
relative to a moderate scalar interpolant on a complex bulk strip.
In particular (33) supplies no zeros of that latter mismatch at
physical endpoint parameters, and supplies no uniform-in-\(N\)
bound on its coefficients.

## 6. Scope and direct sources

The ordinary residual, terminal subtraction, uniqueness, and
parameter ladder retain the original signed power and all physical
normals. All their coefficients may be differentiated in ordinary
exterior parameters before any remaining original trace is taken.
No free endpoint has been replaced by a canonical quotient value.
The identities hold for arbitrary complex \(w\); the microscopic
substitution is used only in Section 5. The total-degree and
Chebyshev-ladder statements concern the single-kernel leaf;
the product corollary does not assert their analogues for products.

The formulas above do not estimate the inverse in (23). Polynomial
uniqueness does not exclude large connection coefficients, and a
local solution of the difference equation has not thereby been
shown to have moderate amplitude. Nor does cancellation of the
\(P_N(Z)\) residual establish equality between an independently
interpolated normal channel and the derivative of a moderate scalar
value interpolation. These analytic questions remain separate.

The three complete direct sources were read at their unchanged
pins, with the used implications and hashes checked:

* [Original finite-band operators and source forcing](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb:
  full algebra, endpoint carrier, signed conjugations, original
  kernel equation and terminal parameter derivative.
* [Ordinary signed difference lifts](research_terminal_twist_bulk_transfer_bound.md),
  SHA256 fca96865315f21dc9961be89061cc6c3a292b2b563e7ded756e86c3438ef5bde:
  ordinary \(J,D_n\), ordered recurrence, preservation of \((P_N)\),
  and the distinction between an ordinary residual and physical jets.
* [Full triangular flag and ordinary reproducer](research_full_endpoint_unit_turn_identities.md),
  SHA256 e2f69aaff28080b9dd9e11365ce18d68a9d738667917204714556681c50789e8:
  terminal Newton ideals, original crossing normalization and
  the exact divided-difference reproducer used in (20).

Only written mathematics, text reads and hashes were used.
No mathematical program, numerical experiment, test or build was
run. Adopted notes and public manuscripts are unchanged.
