# Marked-mode observations retain every actual plat source

24 November 2026. Written research proof.

The endpoint observations underlying the calibrated marked modes are
faithful on the entire actual invariant source, at every fixed even
width. They admit an explicit reconstruction with norm \(e^{C_bN}\).
The proof uses a finite \(q\)-binomial inverse for the original
\(E,K\) action. It needs neither a projective decomposition nor
successive inversions of ill-conditioned weight maps.

At four heads these observations are exactly the previously calibrated
marked-mode coordinates, after one specified original crossing. Thus
they retain the complete \(N\)-dimensional source, including all pair
Casimir normal directions. At greater width their image has explicit
source constraints; it is not a free array of coideal labels.
The original closing functional is transported through the full inverse.
Faithfulness does not give a lower bound for its scalar after an
arbitrary fixed short partial filling.

## 1. Actual endpoint maps and the theorem

Use the root and physical conventions of [M,P,N,H,K,D]:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1}=q^d,\quad \theta=\pi/(2N).
 \tag{1}
\]
On \(V=\mathbb C^N\), in its original orthonormal basis,
\[
 \begin{split}
 E|a\rangle&=(Q^{-a}-1)|a-1\rangle,&
 F|a\rangle&=(1-Q^{a+1})|a+1\rangle,\\
 K|a\rangle&=xQ^{-a}|a\rangle,&
 H|a\rangle&=(d-2a)|a\rangle .
 \end{split}                                                   \tag{2}
\]
Missing endpoint arrows vanish. The actual coproducts are
\[
 E_{12}=E_1K_2+E_2,\quad
 F_{12}=F_1+K_1^{-1}F_2,\quad K_{12}=K_1K_2 .
 \tag{3}
\]
The unrolled \(H\) is additive. All physical norms below are
unnormalized Euclidean or Hilbert--Schmidt norms.
The root \(q\)-binomial identity gives \(E_{\rm tot}^N=F_{\rm tot}^N=0\).
On an even number of heads \(K_{\rm tot}^N=1\). These identities
hold on the whole physical middle module used below.

Put \(c=1+q\) and \(\sigma=-q^{-1}-q^2\). Define two explicit rows
\[
 \eta_a=\frac{1-q^3}{2}q^{3a},\qquad
 \zeta_a=\frac{1-q^{-3}}2x^a,\qquad 0\le a<N .
 \tag{4}
\]
They retain the original root branches; \(q^3\ne1\) at every level
under consideration.
For \(b\ge2\) even, let
\(\mathcal I_b=\operatorname{Inv}_{E,F,K,H}(V^{\otimes b})\)
be the complete root invariant space of [M], with total \(H=0\).
The observation is
\[
 \mathscr D_b=(\eta\otimes I_{V^{\otimes(b-2)}}\otimes\zeta)
                         \big|_{\mathcal I_b}.
 \tag{5}
\]
For \(b=2\) the middle tensor factor means \(\mathbb C\).

**Theorem.** The map (5) is injective at every \(N\ge2\).
Its inverse on its image is explicit, and for each fixed even \(b\)
there is a constant \(C_b\), independent of \(N\), such that
\[
 \|\Phi\|_{\rm ph}\le e^{C_bN}\|\mathscr D_b\Phi\|_{\rm ph}
                      \qquad(\Phi\in\mathcal I_b).
 \tag{6}
\]
The same assertion holds on the actual saturated generic source
\(\mathcal S_b\subset\mathcal I_b\). No generic source condition
is removed in making this restriction.
On the full physical tensor product, before restriction, the row norm is
\[
 \|\eta\otimes I\otimes\zeta\|
         =N\sin^2(3\theta)\le C/N .
 \tag{7}
\]
Thus the pullback of the observed physical norm is a known positive
metric on the actual source, with logarithmic condition \(O_b(N)\).
No polynomial condition bound is asserted.

## 2. Literal currying and its rank-one input

The actual cups and caps are
\[
 p_{ab}=Nx^{-b}\delta_{a+b,d},\quad
 \ell_{ab}=x^a\delta_{a+b,d}/N,\quad
 m_{ab}=x^b/N^2 .
 \tag{8}
\]
In particular \(m\) has no degree delta. The two snake identities
for \(p,\ell\) are the original ones; \(mp=1\) and \(\ell p=0\).
No marked cap is replaced by an ordinary cap below.

Let \(A=V\otimes V\), and let \(W=V^{\otimes(b-2)}\) with the
actual total operators. Rigid duality with exactly (8) identifies
\[
 \operatorname{Hom}_{E,F,K,H}(A,W)\longrightarrow\mathcal I_b,
 \qquad
 f\longmapsto\Phi_f=(I\otimes f\otimes I)(p_{12}\otimes p_{34}).
 \tag{9}
\]
Here the two middle inputs of the four-head expression are replaced
by the complete output \(W\); the order of the two outer heads is fixed.
The inverse is contraction with the corresponding literal caps.
The Hopf and \(H\) equations pass through these snake identities,
so both directions preserve the stated intertwiner conditions.

There is also an entrywise verification fixing all scalars.
Let \(P_{ab}=p_{ab}\), and regard the two input indices of \(f\)
as a matrix for each output index \(i\). Then
\[
 (\Phi_f)_{a,i,b}=(Pf_iP)_{ab}
       =N^2x^{a-b-d}f_{i,d-a,d-b},\qquad
                         \|\Phi_f\|_{\rm ph}=N^2\|f\|_{\rm HS}.
 \tag{10}
\]
The inverse uses \(P^{-1}\) twice. These matrices have singular
values \(N\) and \(1/N\), respectively.

The observation is consequently evaluation at one specified pair vector:
\[
 \mathscr D_b\Phi_f=f(\mathbf u),\qquad
 \mathbf u=(\eta P)\otimes(P\zeta)
             =C_D\sum_{a,b=0}^d\tau^a|a,b\rangle ,
 \tag{11}
\]
\[
 \tau=-Q^{-1},\qquad
 C_D=N^2\sin^2(3\theta)\,q^{3d}.
 \tag{12}
\]
Indeed \((\eta P)_a=N(1-q^3)q^{3d}\tau^a/2\), while
\((P\zeta)_b=N(1-q^{-3})/2\), independent of \(b\).
The factor \(C_D\) is nonzero and bounded above and below in modulus
by universal constants: \(2\le|C_D|\le9\pi^2/4\).
This includes \(N=2\), when \(C_D=-2i\),
and \(N=3\), when \(\sigma=0\) and \(C_D=9\).
Also \(\|\eta\|=\|\zeta\|=\sqrt N\sin(3\theta)\), proving (7).

We next prove that this exact \(\mathbf u\), rather than a favorable
replacement, is cyclic already for the \(E_A,K_A\) action.

## 3. A finite \(q\)-binomial orbit basis

Identify functions on the pair grid with
\[
 \mathscr R=\mathbb C[X,Y]/(X^N-1,Y^N-1),\qquad
 X=Q^{-(a+b)},\quad Y=Q^{-b}.
 \tag{13}
\]
The change from \((a,b)\) to these two clocks is a permutation.
The monomials \(X^sY^r\), \(0\le r,s<N\), are an orthogonal
Fourier basis, each of norm \(N\).

Set
\[
 R=Q^{-1},\qquad \mathfrak c=x\tau=q^{-3},\qquad
 \alpha=\mathfrak cR .
 \tag{14}
\]
Divide a pair vector by its nonzero entries \(C_D\tau^a\).
The original total \(E_A\) then acts by the exact operator
\[
 \begin{split}
 (\mathcal L P)(X,Y)
   ={}&\alpha X P(RX,Y)-\mathfrak cY P(RX,Y)\\
      &+(RY-1)P(RX,RY).
 \end{split}                                                   \tag{15}
\]
For the first term use \(E_1K_2\), with input \(a+1,b\);
for the second-head term the input is \(a,b+1\).
Their missing endpoint arrows are zero because their displayed
coefficients vanish there. Thus (15) is a grid identity including
all endpoints, not an extension past the physical boundary.
Put \(f_r=\mathcal L^r1\). Then
\[
 E_A^r\mathbf u=\mathbf u\,f_r(X,Y),\qquad
 K_A=Q^{-1}X .
 \tag{16}
\]

For \(n,k<N\) define the finite products
\[
 L_k=\prod_{j=1}^k(R^j-\mathfrak c),\qquad
 N_n(X)=\prod_{j=0}^{n-1}(\alpha R^jX-1),\qquad
 \widetilde N_n(X)=\prod_{j=0}^{n-1}(R^j-\alpha X).
 \tag{17}
\]
Empty products are one. Each factor of \(L_k\) is nonzero:
\(R^j\) is an even power of \(q\), whereas \(\mathfrak c=q^{-3}\)
is an odd power.
Let \({r\brack k}_R\) be the Gaussian binomial polynomial.

The exact forward and inverse identities are
\[
 \boxed{\quad
 f_r(X,Y)=\sum_{k=0}^r {r\brack k}_R
                     L_kY^kN_{r-k}(X),\qquad 0\le r<N ,
 \quad}                                                        \tag{18}
\]
\[
 \boxed{\quad
 L_rY^r=\sum_{k=0}^r{r\brack k}_R
                     \widetilde N_{r-k}(X)f_k(X,Y).
 \quad}                                                        \tag{19}
\]
In particular \(f_r\) has \(Y\)-degree \(r\), with constant
leading coefficient \(L_r\). Hence
\[
       \{(QK_A)^sE_A^r\mathbf u:0\le r,s<N\}
                   \quad\hbox{is a basis of }A .               \tag{20}
\]

Here are finite proofs of both identities. Applying (15) to
\(P(X)Y^k\) gives
\[
 P(RX)\bigl[(\alpha X-R^k)Y^k+
                         (R^{k+1}-\mathfrak c)Y^{k+1}\bigr].
 \tag{21}
\]
Use \(L_k=(R^k-\mathfrak c)L_{k-1}\) and
\(N_{n+1}(X)=(\alpha X-1)N_n(RX)\).
The two Gaussian Pascal identities
\[
 {r+1\brack k}_R={r\brack k}_R+R^{r+1-k}{r\brack k-1}_R
             =R^k{r\brack k}_R+{r\brack k-1}_R
 \tag{22}
\]
then prove (18) by induction, including its lower and upper terms.

For the inverse, work with formal series only modulo \(z^N\).
Every denominator \((R;R)_n\), \(n<N\), is nonzero. The product
recurrences show that
\[
 D(z)=\sum_{n<N}\frac{N_n(X)}{(R;R)_n}z^n,\quad
 \widetilde D(z)=\sum_{n<N}
                    \frac{\widetilde N_n(X)}{(R;R)_n}z^n
 \tag{23}
\]
satisfy
\[
 (1+z)D(z)=(1+\alpha Xz)D(Rz),\qquad
 (1+\alpha Xz)\widetilde D(z)=(1+z)\widetilde D(Rz)
                       \pmod {z^N}.
 \tag{24}
\]
Their product is \(R\)-invariant, with constant one. Since
\(1-R^n\ne0\) for \(0<n<N\), it equals one modulo \(z^N\).
Thus the corresponding finite Gaussian convolution is the identity.
Substitute (18), and use
\({r\brack k}_R{k\brack j}_R={r\brack j}_R{r-j\brack k-j}_R\);
this proves (19). No denominator \((R;R)_N\), infinite product
or limiting root prescription is used.

## 4. Quantitative reconstruction without a product of losses

The same finite formulas give an exponential, rather than
\(e^{CN\log N}\), bound for the full inverse.
The complete odd-grid product is exactly
\[
 \prod_{j=1}^N|R^j-\mathfrak c|
                    =|1-\mathfrak c^N|=2 .
 \tag{25}
\]
Every factor is at most two. Therefore, for \(k<N\),
\[
                  2^{\,k-N+1}\le|L_k|\le2^k .
 \tag{26}
\]
On \(|X|=1\), both \(N_n,\widetilde N_n\) have coefficient
absolute sum at most \(2^n\). Also
\[
                  |{r\brack k}_R|\le {r\choose k}.
 \tag{27}
\]
The last inequality follows from the nonnegative integer
coefficients of the Gaussian polynomial, obtained recursively
from (22). Thus every conditional matrix in (18) and its inverse
(19), evaluated at a clock value of \(X\), has norm \(e^{CN}\).
Using normalized Fourier transforms first in \(X\) and then in \(Y\)
proves the same condition bound for (20). The two unnormalized
value transforms contribute \(N\) to the forward matrix and
\(1/N\) to its inverse. They contribute no exponential loss.

For subsequent source use it is helpful to give the reconstruction
operators themselves. At a physical pair index \((a,b)\) put
\(X_{ab}=Q^{-(a+b)}\), \(Y_b=Q^{-b}\), and define
\[
 \begin{split}
 \mathscr R_{ab}
 =\frac1{N^2}\sum_{s,r=0}^d
 X_{ab}^{-s}Y_b^{-r}(QK)^s L_r^{-1}
       \sum_{k=0}^r {r\brack k}_R
                    \widetilde N_{r-k}(QK)E^k .
 \end{split}                                                   \tag{28}
\]
Operator factors are in the displayed order. Equations (16),(19)
and the two Fourier inversions give
\[
                  \mathscr R_{ab}^{A}\mathbf u
                       =C_D\tau^a|a,b\rangle .
 \tag{29}
\]
The superscript indicates the actual module on which a word acts.
These are weighted coordinate reconstructors on this cyclic input;
they have not been asserted to be orthogonal matrix units.

Each expression (28) is a linear combination of words in \(E,K\)
of length \(O(N)\), with coefficient absolute sum \(e^{CN}\).
For example the inner sum has coefficient bound \(3^r\);
combine it with (26) and the two normalized finite Fourier sums.
Only \(K^N=1\), \(E^N=0\), and \(KE=QEK\) are needed.

On a fixed \(n\)-head physical middle module,
\(\|E_W\|\le2n\), \(\|K_W\|=1\). Hence
\[
                  \|\mathscr R_{ab}^{W}\|\le e^{C_nN}.
 \tag{30}
\]
If \(f:A\to W\) intertwines \(E,K\), (29) implies
\[
 f|a,b\rangle
       =(C_D\tau^a)^{-1}\mathscr R_{ab}^{W}f(\mathbf u).
 \tag{31}
\]
There are only \(N^2\) such vectors. Combining (10),(30),(31)
proves (6), with all polynomial powers of \(N\) absorbed into
the stated \(e^{C_bN}\).
In fact evaluation at \(\mathbf u\) is injective for every
\(E,K\)-intertwiner, before imposing \(F\) or \(H\).

## 5. The exact image, including the unrolled constraint

The image need not be guessed from a dimension comparison.
The algebra generated by \(E,K\), with
\(E^N=0,K^N=1,KE=QEK\), is spanned by its \(N^2\) ordered
monomials. Their independent orbit (20) proves that the pair is
its regular cyclic module with cyclic vector \(\mathbf u\).
Consequently every \(y\in W\) specifies a unique \(E,K\)-intertwiner
\(f_y:A\to W\), given explicitly by (31).

Write the actual coideal operator as
\[
                 B_\sigma=F-EK^{-1}+\sigma K^{-1}.
 \tag{32}
\]
The exact seed relation is
\[
                        B_\sigma^A\mathbf u=\sigma\mathbf u .
 \tag{33}
\]
For a direct check, the one-head vector \(\mathbf1\) has
\(B_\sigma\)-eigenvalue \(c\), while \((\tau^a)_a\) has
\(B_c\)-eigenvalue \(\sigma\). Substitute (2) and
\(\sigma=-q^{-1}-q^2\); the coefficients of \(Q^a\) cancel.
The coproduct identity
\(B_\sigma^{12}=F_1-E_1K_1^{-1}+K_1^{-1}B_\sigma^2\)
then proves (33), including both endpoints.

An \(E,K\)-intertwiner \(f_y\) also intertwines \(F\) if and only if
\[
                         (B_\sigma^W-\sigma I)y=0 .
 \tag{34}
\]
Necessity follows from (33). For sufficiency let
\(\Delta=f_yF_A-F_Wf_y\). The actual commutator
\([E,F]=(q-q^{-1})(K-K^{-1})\) gives
\(\Delta E_A=E_W\Delta\) and
\(\Delta K_A=QK_W\Delta\).
Condition (34) is exactly \(\Delta\mathbf u=0\), using (33).
Thus \(\Delta\) vanishes on the whole basis (20).
This proves (34) without a full quantum-group PBW or a
projective decomposition assumption.

The unrolled condition is also explicit. Put
\[
 \mathfrak a_H=\sum_{a,b=0}^d(2d-2a-2b)\mathscr R_{ab}.
 \tag{35}
\]
The weighted normalization in (29) is important:
\(\mathfrak a_H^A\mathbf u=H_A\mathbf u\).
No extra factor \(C_D\tau^a\) is inserted in (35).
For an \(E,F,K\)-intertwiner, the defect
\(H_Wf_y-f_yH_A\) is again an \(E,F,K\)-intertwiner, by the
two commutators with \(H\). It therefore vanishes if and only
if it vanishes at \(\mathbf u\).
We obtain the exact image description
\[
 \boxed{\quad
 \mathscr D_b(\mathcal I_b)=
 \{y\in W:(B_\sigma^W-\sigma I)y=0,\quad
                      (H_W-\mathfrak a_H^W)y=0\}.
 \quad}                                                        \tag{36}
\]
For such \(y\), the inverse is the literal \(\Phi_{f_y}\) of
(9)--(10), not a freely prepared boundary vector.
All coefficients in (35) are known and have word bounds \(e^{CN}\).

For the actual saturated generic source, [D]'s value theorem adds
the specified regular divided-current condition:
\[
 \mathscr D_b(\mathcal S_b)=
 \{y\text{ satisfying (36)}:
                 \mathcal J_E^{(b)}\Phi_{f_y}=0\}.
 \tag{37}
\]
This keeps the entire original operator on the reconstructed
invariant tensor; it does not presume a new divided-current
identity on a free coideal clock. The corresponding
\(\mathcal J_F\) condition is redundant on the actual source,
as proved in [D].
When the whole parameter-dependent source is differentiated,
its actual inhomogeneous normal Ward equations must still be
retained. Equation (37) is not a homogeneous assertion for those jets.

At \(b=4\), [M,D] give
\(\mathcal S_4=\mathcal I_4\), of dimension \(N\).
For \(b\ge6\), neither the unrolled condition in (36) nor the
saturated-source condition in (37) is dropped. The coideal
kernel by itself is generally larger.

## 6. Why these are the calibrated marked-mode observations

We verify the endpoint interpretation without moving the marked cap.
On an invariant tensor, the recursive coideal and the equations
\(E_{\rm tot}=F_{\rm tot}=0,K_{\rm tot}=1\) give
\[
 B_c^{(2,\ldots,b)}\Phi=C_1\Phi,\qquad
                 C=cK-KF+KEK^{-1}.
 \tag{38}
\]
One may multiply the recursion by \(K_1\) to obtain this formula.
The actual cup gives \(CP=PB_c^{\mathsf T}\), so \(C\)
has the same simple coideal spectrum as \(B_c\).
Direct substitution also gives
\[
 C\mathbf1=\sigma\mathbf1,\qquad
 \eta C=\sigma\eta,\quad\eta\mathbf1=1,\qquad
 B_c(\tau^a)_a=\sigma(\tau^a)_a,\quad
 \zeta B_c=\sigma\zeta,\quad\zeta(\tau^a)_a=1 .
 \tag{39}
\]
For instance the two normalizing sums are
\(\sum q^{3a}=2/(1-q^3)\) and
\(\sum q^{-3a}=2/(1-q^{-3})\).

It follows that (5) selects the first and last coideal heights
\(\sigma\) in the complete nested height expansion of an
actual invariant tensor. The remaining middle vector lies in
\(\ker(B_\sigma^W-\sigma I)\), in agreement with (36).
The one-head graph eigenvectors
\[
                 u_\lambda(\rho)_a
                   =q^{-a}D_a(\lambda;\rho)/F_a
 \tag{40}
\]
have first coordinate one. Thus no further scalar is hidden
when the remaining observations are read in that height basis.

For completeness these fixed-width physical-to-height frame
changes and their inverses have norm \(e^{C_bN}\).
The continuant recurrence bounds \(D_a(\lambda;\rho)\) by \(C^a\)
for \(|\lambda|,|\rho|\le2\). Since
\(\prod_{a=1}^d(1-Q^a)=N\), every partial product has inverse
at most \(2^{d-a}/N\). This bounds (40).
The inverse row is
\((E_d(\lambda;\rho)/p_N'(\lambda))(D_a/F_a)_a\);
its extra factor has modulus \(\sin\alpha_\lambda\le1\),
as in [N,K]. Iterating these finite frame changes a fixed
number of times proves the claimed \(e^{C_bN}\) bound.
This is a controlled exponential change, not an assumed
polynomial equivalence with the physical metric.

Now specialize to four heads. Expand an actual invariant \(\Phi\)
with external height \(c\). At last height \(\sigma\), let
\(v_l(\nu)\) be its slice at the neighboring height
\(\rho=\mu_l\). Use exactly [N]'s calibrated row \(r_l\)
and constant
\[
 C_0=r_ls_l=\frac{2\kappa}{1-q^3},\qquad
 \kappa=q^{d^2/2},\qquad
                 a_l=\frac{r_lv_l}{C_0}.
 \tag{41}
\]
The source identity \(r_lB^+_{c,\rho}=C_0e_*^{\mathsf T}\)
proves
\[
 a_l=e_*^{\mathsf T}B^-_{c,\rho}v_l .
 \tag{42}
\]
Hence \(a=(a_l)_l\) is precisely the remaining height coordinate
vector of
\[
                         \mathscr D_4 R_{12}^-\Phi .
 \tag{43}
\]
The original crossing is invertible and preserves the complete
root invariant and saturated source spaces. The target coideal
kernel on the middle two heads has dimension \(N\), by its
graph recurrence. Together with (6), (36), and the dimension
in [M,D], this proves that (41) is an isomorphism on the
entire four-head actual source, at every level.

Its inverse, in the specified physical source and raw height
coordinates, has norm \(e^{CN}\). In addition to (6), the
only fixed crossing in (43) has the exact conditional matrices
\(\kappa U_\rho^{-1}\mathcal D\overline{U_c}\) of [N,H];
(40) and its inverse bound control these and their inverses
by \(e^{CN}\). No inverse of an unknown word is used.

Most importantly the original readout after the literal
cap-straddling crossing is still
\[
       (\ell_{12}\otimes m_{34})R_{23}^+\Phi
                      =\beta_N C_0\sum_{l=0}^d a_l .
 \tag{44}
\]
All factors in \(\beta_N\) are the original ones in [N,H].
An original external \(\chi_N\) remains a further multiplier.
To restore the original bare closing in (44), retain \(R_{23}^-\)
in the word; \(R_{12}^-\) is already part of the observation coordinates.
This is an exact transport, not a change in its framing or mark.

## 7. General words, source constraints, and remaining scope

For any fixed even width, let
\(\mathcal Y_b=\mathscr D_b(\mathcal S_b)\) be the constrained
image (36)--(37). Every original regular signed braid gives
the strict transported map
\[
               \widetilde R_i
                   =\mathscr D_bR_i\mathscr D_b^{-1}
                             \quad\hbox{on }\mathcal Y_b .
 \tag{45}
\]
Products of these maps equal the transport of the whole product.
The original cup source is \(\mathscr D_b(p^{\otimes b/2})\).
The original last-mark row is its literal composition with
the reconstructed \(\Phi_{f_y}\); no positive trace or
favorable observation is substituted for it.
The inverse and metric bounds are \(e^{C_bN}\), not
small-error estimates for arbitrary transported states.

In particular, replacing every raw slice by its independent
marked-mode projection need not produce an invariant tensor.
Faithful coordinates must be reconstructed by (31),(36),(37).
At greater width the remaining labels are subject to those
conditions, even though all of them appear in a height array.
The result does not authorize projecting before a later
crossing without this exact full-source reconstruction.

[M] already constructs complete all-width source modules and
original cap rows, and [P] proves the full pair commutant.
[D] already distinguishes the saturated source from the
larger root invariant space. Neither the existence of a full
frame nor those source restrictions are claimed new here.
The addition is faithfulness and a controlled reconstruction
for these particular marked-mode observations, which are the
ones carrying [N,H]'s calibrated source data.
The finite Gaussian-binomial and Fourier tools themselves
are standard; all root conventions and inverse factors are
fixed above by the actual matrices.

Every pair-Casimir derivative channel remains in the reconstructed
physical tensor. No geometric trial field, common positive
scalar pairing, or noncancellation under arbitrary coherent
exteriors has been proved. The full finite-exception volume
target after arbitrary fixed short partial fillings remains open.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| M | [Complete original source multiplicities](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_complete_source_multiplicity_module.md) | 602 | 14cfb558f50c5b091cec9439692dfeb87129e31f38588cb1ebfd8e8547ac99a9 |
| P | [Full physical pair commutant](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_pair_casimir_commutant_and_rotated_trace.md) | 331 | 00ab946b3eddb61256bdbd8ec487789a15991a80e1a28b4eee53bbb4a00f7666 |
| N | [Marked-boundary normal gap](research_coideal_marked_boundary_normal_gap.md) | 512 | bb9bd6d04480ae8733c0fd1c5901834bdf2ea3e8c7eb3617fb8eb58e66e57956 |
| H | [Height pairing and original boundary](research_coideal_height_pairing_and_marked_boundary.md) | 543 | bed81fcb12b20d16d41c55b476b13d8d69b1fe79d0d0620c31230ba652b1d82f |
| K | [Continuant source kernel](research_coideal_continuant_source_kernel.md) | 365 | 3ea997e5258c9413fd7c771a6a1475b90b39bf731ac55c0902fd136943b26f44 |
| D | [All-width divided-current source restriction](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_all_width_divided_source_projection.md) | 204 | dc83b5e232a3d258f516a479d7257e85b9e5663a38e166f07c6ad9ae81004a68 |

Only written mathematics, source reads and text/hash operations were used.
Earlier final notes, the ledger and public manuscripts are unchanged.
