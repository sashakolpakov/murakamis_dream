# Balanced marked observations at every coideal height

24 November 2026. Written research proof.

A balanced physical clock charge moves the last marked observation to
any coideal height. On the actual closed source its change is a known
unit, because the other ordinary caps fix the degree of the final pair.
This gives a two-label auxiliary family for every original signed word,
with all shared-height sums retained. Its whole-word coefficient is the
original scalar, which is allowed to vanish.

At a matched bottom height the selected two-head vector and graph row
are explicit geometric sequences. Their counting norms and overlap are
known before the word is evaluated. The resulting clock moments retain
the finite endpoint exactly. The literal scaled lowering operator also
has a locally uniform analytic initializer limit, the transform of an
explicit positive exponential density. These statements do not evaluate
the global quartic minimum or identify a contributing geometric cycle.

## 1. Original tensors and the full source

Use the complete conventions of H,T,A below. Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1}=q^d,\quad F_a=(Q;Q)_a,
 \quad (z;Q)_a=\prod_{j=0}^{a-1}(1-zQ^j).
 \tag{1}
\]
Empty products are one. The physical basis \(e_0,\ldots,e_d\) is
orthonormal. Its original one-head generators are
\[
 Ke_a=xQ^{-a}e_a,\qquad Ee_a=(Q^{-a}-1)e_{a-1},\qquad
 Fe_a=(1-Q^{a+1})e_{a+1},
\]
with absent endpoint arrows zero.
The clock is \(\mathcal Qe_a=Q^ae_a\). The literal cup, ordinary cap
and last marked cap have coefficients
\[
 \mathbf p_{ab}=Nx^{-b}\mathbf1_{a+b=d},\qquad
 \ell_{ab}=\frac{x^a}{N}\mathbf1_{a+b=d},\qquad
 m_{ab}=\frac{x^b}{N^2}.
 \tag{2}
\]
In particular the marked row has no degree delta.
For width \(2k\), \(k\ge1\), write
\[
 u_0=\mathbf p^{\otimes k},\quad
 \ell_0=\ell^{\otimes(k-1)}\otimes m,\quad
 Z_N(R)=\ell_0Ru_0,\qquad K_N=\chi_N Z_N(R).
 \tag{3}
\]
Here \(R\) is any original unmarked signed braid word.
The separate original factor \(\chi_N\) remains external.
No division by \(Z_N(R)\) or \(\chi_N\) is used.

Use the continuants and their normalized vectors
\[
 D_{-1}=0,\quad D_0=1,\qquad
 D_{a+1}(\lambda;\sigma)
 =(\lambda+qQ^a\sigma)D_a-q(1-Q^a)^2D_{a-1},
\]
\[
 u_\lambda(\sigma)_a
      =q^{-a}D_a(\lambda;\sigma)/F_a,\qquad
 \Phi_{\lambda,\sigma}(z)
      =\sum_{a=0}^dD_a(\lambda;\sigma)z^a/F_a.
 \tag{4}
\]
Let \(\mu_l=Q^l+qQ^{-l}\), \(0\le l<N\), be the simple coideal roots,
and put
\[
 p_N(z)=\prod_{l=0}^{N-1}(z-\mu_l),\qquad
 A_\lambda=\frac{N^2q^dx^{-d}}{p_N'(\lambda)}.
 \tag{5}
\]
All these \(A_\lambda\) are nonzero. The full nested frame of A has
columns
\(\bigotimes_{j=1}^{2k}u_{\nu_{j-1}}(\nu_j)\), with
\(\nu_{2k}=\sigma\), before the external channel is restricted to
\(\nu_0=\sigma\). It retains all \(N^{2k}\) coordinates and the
original Casimir normal data.

## 2. A legal balanced charge on the last mark

For an integer \(r\), taken modulo \(N\), define
\[
 m_r=m(\mathcal Q^r\otimes\mathcal Q^r),\qquad
 (m_r)_{ab}=\frac{x^bQ^{r(a+b)}}{N^2}.
 \tag{6}
\]
The actual word preserves integer degree. The source has degree \(kd\),
and each of the first \(k-1\) ordinary caps forces pair degree \(d\).
Consequently the last pair has degree \(d\) in every surviving term,
and hence
\[
 \boxed{\quad
 (\ell^{\otimes(k-1)}\otimes m_r)Ru_0
                    =Q^{rd}Z_N(R).
 \quad}                                                       \tag{7}
\]
This is an equality on the specified physical source. It does not
replace the marked row by another row on the whole tensor space.
All original orderings and phases are retained.

For a physical bottom root \(\sigma\), the charged diagonal seam is
\[
 m_r[u_\sigma(\lambda)\otimes u_\lambda(\sigma)]
 =\frac1{N^2}
 \overline{\Phi_{\lambda,\sigma}(-qQ^{-r})}
                  \Phi_{\lambda,\sigma}(-q^{-2}Q^r).
 \tag{8}
\]
To verify the conjugate factor, T's reciprocity and
\(\overline{F_a}=(-1)^aq^{-a(a+1)}F_a\) give
\(D_a(\sigma;\lambda)/F_a=(-1)^a
\overline{D_a(\lambda;\sigma)/F_a}\).
This applies to actual roots and gives (8) directly from (2),(6).

Put
\[
 \lambda_r=-q^{2r-1}-q^{2-2r},\qquad
 T_r=\frac{Q^{rd}}{A_{\lambda_r}}.
 \tag{9}
\]
The \(\lambda_r\), \(0\le r<N\), are exactly all the physical roots.
We claim the all-bottom identity
\[
 \boxed{\quad
 m_r[u_\sigma(\lambda)\otimes u_\lambda(\sigma)]
                    =\delta_{\lambda,\lambda_r}T_r
 \quad}                                                       \tag{10}
\]
for every physical \(\sigma,\lambda\), including \(N=2\).

Here is the finite support proof. Write \(\lambda=\mu_j,\sigma=\mu_l\),
\(h=\lfloor N/2\rfloor\). T's exact product is
\[
 \Phi_{\lambda,\sigma}(z)
   =(-qQ^lz;Q)_a(-q^2Q^{-l}z;Q)_b,\quad a+b=d,
\]
where \(a=[h-j-l]_N\) for even \(N\), and
\(a=[h+j-l]_N\) for odd \(N\).
At the two arguments in (8) its even-power strings are
\[
 (Q^{l+1-r};Q)_a,\qquad (Q^{r-l};Q)_b.
\]
The other strings have odd powers of \(q\), so none of their factors
vanishes. The displayed strings are nonzero exactly when
\[
 a\le[r-l-1]_N,\qquad b\le[l-r]_N.
\]
The two right sides add to \(d\). Thus both survive only at
\(a=[r-l-1]_N,\ b=[l-r]_N\).
This gives \(j=[h+1-r]_N\) for even \(N\) and
\(j=[r-h-1]_N\) for odd \(N\), precisely the root in (9).
Both index maps are bijections. Empty strings cause no exception.

For the coefficient use H's literal cup expansion
\[
 \mathbf p=\sum_\lambda A_\lambda\,
                u_\sigma(\lambda)\otimes u_\lambda(\sigma).
\]
The left side has \(m_r\mathbf p=Q^{rd}\). The unique surviving
term therefore has coefficient \(T_r\) in (9), with its full phase.
No mark relocation or favorable phase choice is used.

## 3. Every last height observes the original whole-word scalar

Set \(p=k-1\). In A's external \(\sigma\) block the cup column is
\[
 a_\sigma(\boldsymbol\nu)
  =\prod_{i=1}^kA_{\nu_{2i-1}}
        \prod_{i=1}^{k-1}\delta_{\nu_{2i},\sigma}.
\]
For any physical last height \(\lambda\), let the ordinary linear row
\[
 b_{\sigma,\lambda}(\boldsymbol\nu)
   =\delta_{\nu_{2k-1},\lambda}
        \prod_{i=1}^{k-1}\delta_{\nu_{2i},\sigma}
\]
leave every other odd height summed. As in A, form the full frame
first and then let
\(\mathcal R_\sigma=(\Psi_\sigma^{-1}R\Psi_\sigma)|_{\nu_0=\sigma}\).
The original commutation and source identities in A justify this
restriction. No intermediate projector is inserted.

Ordinary-cap sewing and (10) identify the charged physical row on
this block as \(T_rA_\sigma^{-p}b_{\sigma,\lambda_r}\).
Combine this with (7) and cancel the specified nonzero \(T_r\).
Since (9) covers every root, the result is
\[
 \boxed{\quad
 \mathcal S_{\sigma,\lambda}(R)
 :=b_{\sigma,\lambda}\mathcal R_\sigma a_\sigma
       =A_\lambda A_\sigma^p Z_N(R)
 \quad}                                                       \tag{11}
\]
for every pair of physical roots \((\sigma,\lambda)\).
Every shared internal-height sum remains inside
\(\mathcal S_{\sigma,\lambda}\).

For the sorted root angle
\(\lambda=2\sqrt q\cos\alpha_\lambda\),
\(0<\alpha_\lambda<\pi\), H,T give
\(|A_\lambda|=N\sin\alpha_\lambda\in[1,N]\).
Thus, including zero scalars,
\[
 |Z_N(R)|\le|\mathcal S_{\sigma,\lambda}(R)|
                              \le N^k|Z_N(R)|.
 \tag{12}
\]
The choices of both root labels are unrestricted by this scalar
comparison. It is a polynomial cost at fixed width, even for
macroscopic changes of the two indices.

More explicitly put
\(w_j=Q^j-qQ^{-j}\) and
\(\gamma_N=(N/2)q^dx^{-d}\).
Since \(A_{\mu_j}=\gamma_Nw_j\), (11) is the exact root-grid family
\[
 \mathcal S_{\mu_l,\mu_j}(R)
          =\gamma_N^k Z_N(R)w_jw_l^p.
 \tag{13}
\]
Its two Laurent degrees are \(1,p\), fixed by width rather than
word length. Aliases at small \(N\) are retained by evaluating this
polynomial on the root grid, as in A; no off-grid identity is asserted.
This refines the one-label closed family of A, rather than reducing
the rank of an open component or the full physical source.

The same boundary counting as in A remains polynomial uniformly in
both labels. If \(\theta=\pi/(2N)\) and \(a_\eta=\sin\alpha_\eta\),
the absolute-height metric has
\[
 \|u_0\|_{G_{\rm ht,\sigma}}^2
       =[N^2\csc\theta/a_\sigma]^k,\qquad
 \|\ell^{\otimes p}\otimes m_r\|_{\rm block,dual}^2
       =N^{-2k}\frac{a_\sigma^{\,2-k}\csc^p\theta}
                         {a_{\lambda_r}} .
 \tag{14}
\]
Indeed the row coefficient is \(T_rA_\sigma^{-p}\), with
\(|T_r|=(Na_{\lambda_r})^{-1}\), and its remaining free odd indices
sum exactly as in A. This is the prescribed external block norm,
not a value bound on an arbitrary propagated word state.

## 4. The matched initializer and its literal graph row

Choose the bottom root and the two unit-modulus sequences
\[
 \sigma_r=Q^r+qQ^{-r},\quad
 t_r=xQ^r=-q^{2r-1},\quad
 \beta_r=q^{-1}t_r,\quad B_r=q^{-1}t_r^2=q^{4r-3}.
 \tag{15}
\]
Then \(\lambda_r=t_r+q/t_r\) and
\(\sigma_r=-qt_r-t_r^{-1}\). In particular \(B_r^N=-1\).

The one-head operator \(T_\sigma=F-(E-\sigma)K^{-1}\) has literal
coordinates
\[
 (T_\sigma v)_a=(1-Q^a)v_{a-1}
       +q(1-Q^{a+1})v_{a+1}-q\sigma Q^av_a.
\]
Absent endpoint arrows are zero. Direct substitution gives
\[
 u_{\lambda_r}(\sigma_r)_a=\beta_r^a,\qquad
 h_r=(t_r^a)_{a=0}^d,\qquad
 h_rT_{\sigma_r}=\lambda_rh_r .
 \tag{16}
\]
The first coordinate fixes the right eigenvector normalization.
The reciprocal continuant gives the full first factor
\(u_{\sigma_r}(\lambda_r)_a=Q^{-ra}\).

T's width-two graph with external value \(\sigma\) is
\[
 L_\sigma=\sum_{a=0}^d|a\rangle\otimes
              q^{-a}D_a(\sigma;T_\sigma)/F_a,\qquad \pi_0L_\sigma=I.
\]
It follows exactly that
\[
 \boxed{\quad m_rL_{\sigma_r}=h_r/N,\qquad
 T_r=\frac{2}{N(1-B_r)}.\quad}                               \tag{17}
\]
For proof, substitute (6) and move each polynomial in \(T_{\sigma_r}\)
through its left eigenrow \(h_r\).
The resulting scalar sum is
\(\sum_aq^{-a}Q^{ra}D_a(\sigma_r;\lambda_r)/F_a=N\),
because each summand is one by the reciprocal vector above.
Finally
\(h_ru_{\lambda_r}(\sigma_r)=\sum_aB_r^a=2/(1-B_r)\).
This also calibrates (9)'s coefficient without discarding a phase.

The counting norms of \(h_r\) and \(u_{\lambda_r}(\sigma_r)\) are
both \(\sqrt N\). The normalized graph source/row overlap is
\[
 \frac{|h_ru_{\lambda_r}(\sigma_r)|}
              {\|h_r\|_2\|u_{\lambda_r}(\sigma_r)\|_2}
       =\frac{2}{N|1-B_r|}=|T_r|\ge\frac1N.
 \tag{18}
\]
The full matched pair has norm \(N\), while \(\|m_r\|_2=1/N\);
its observation is the same \(T_r\).
These are known initializer norms, not a lower bound after a word.

All integer clock moments are also specified before propagation:
\[
 \frac{h_r\mathcal Q^ju_{\lambda_r}(\sigma_r)}
                  {h_ru_{\lambda_r}(\sigma_r)}
       =\frac{1-B_r}{1-B_rQ^j},\qquad j\in\mathbb Z.
 \tag{19}
\]
Every denominator is nonzero, including the endpoints and \(N=2\).
For fixed \(j\), these moments tend to one with error \(O_j(N^{-1})\)
whenever \(B_r\) stays a fixed distance from one.
The full first-leg contraction has the separate exact identity
\[
 \frac1N\sum_{a=0}^d Q^{ra}\,Q^{ja}\,
                        u_{\sigma_r}(\lambda_r)_a
           =\mathbf1_{j\equiv0\pmod N}.
 \tag{20}
\]
Thus its uniform finite clock sum is retained along with (19).
No joint physical point or geometric cycle is substituted for these arrays.

## 5. A uniform analytic initializer at the matched endpoint

Let \(\omega_{N,r}(O)=h_rOu/(h_ru)\), where
\(u=u_{\lambda_r}(\sigma_r)\). This is the specified linear cap
functional, not a finite-\(N\) positive state.
Equivalently it is the actual matched pair observation
\[
 \omega_{N,r}(O)=
 \frac{m_r(I\otimes O)
     [u_{\sigma_r}(\lambda_r)\otimes u_{\lambda_r}(\sigma_r)]}{T_r},
\]
since the first-leg contraction in this formula is exactly \(N\).
For \(0\le m<N\), its literal lowering moments are
\[
 \omega_{N,r}(E^m)=
 \beta_r^m
 \frac{\prod_{j=1}^m(Q^{-j}-1)}
      {\prod_{j=1}^m(1-B_rQ^{-j})}.
 \tag{21}
\]
Indeed \(E^mu=\beta_r^m
\prod_{j=1}^m(Q^{-j}\mathcal Q^{-1}-1)u\), including every
zero upper arrow. For the normalized geometric functional
\(\Omega_B(P)=(1-B)\sum_{a=0}^{N-1}B^aP(Q^a)/2\), \(B^N=-1\),
put \(F_m(B)=\Omega_B(\prod_{j=1}^m(Q^{-j}\mathcal Q^{-1}-1))\).
Its finite geometric sum gives
\[
 F_m(B)=Q^{-m}\frac{1-B}{1-BQ^{-1}}F_{m-1}(BQ^{-1})-F_{m-1}(B).
\]
Induction from \(F_0=1\) proves (21): after a common denominator
the new numerator is
\(Q^{-m}(1-B)-(1-BQ^{-m})=Q^{-m}-1\).
All denominators are nonzero odd-root chords. The next numerator
at \(m=N\) is zero, consistently with the actual \(E^N=0\).

Fix a compact interval \(I\subset(1/2,1)\), and write \(\rho=r/N\).
There is a radius \(\varepsilon_I>0\) such that, uniformly for
\(\rho\in I\) and \(|z|\le\varepsilon_I\),
\[
 \boxed{\qquad
 \omega_{N,r}\!\left(e^{zNE}\right)
       =\frac1{1-c(\rho)z}+O_I(N^{-1}),\qquad
 c(\rho)=-\frac{\pi}{\sin(2\pi\rho)}>0 .
 \qquad}                                                       \tag{22}
\]
The finite exponential on the left is its polynomial of degree \(N-1\).
If merely \(r/N\to\tau\in I\), its limit is
\((1-c(\tau)z)^{-1}\); no rate for \(r/N\to\tau\) is assumed.
There is no rotation of the physical observable \(NE\).

Here is a coefficient proof controlling the whole analytic function.
Write \(a_{N,m}=\omega_{N,r}((NE)^m)/m!\) for \(m<N\), and set
it to zero for \(m\ge N\). Formula (21) expresses \(a_{N,m}\) as
the product of
\[
 \frac{N\beta_r(Q^{-j}-1)}{j(1-B_rQ^{-j})},\qquad 1\le j\le m.
\]
Choose \(\eta>0\) below \(\min_{\rho\in I}|1-e^{4\pi i\rho}|\).
For a sufficiently small fixed \(\delta_I>0\), all denominator
chords with \(m\le\delta_I N\) are at least \(\eta/2\), for large \(N\).
Each displayed factor is bounded by a fixed constant \(C_I\)
and differs from \(c(\rho)\) by at most \(C_I(j+1)/N\).
Here its limiting ratio is
\(-2\pi i(-e^{2\pi i\rho})/(1-e^{4\pi i\rho})=c(\rho)\).
Telescoping the product gives
\[
 |a_{N,m}-c(\rho)^m|
                   \le N^{-1}m(m+1)C_I^m
       \quad(m\le\delta_I N).                                \tag{23}
\]

For the remaining coefficients, any \(m\) distinct odd-root chords
have product at least \(m!/N^m\). To see this, order all \(N\)
odd-root chords by distance from one. The \(j\)-th smallest is
\(2\sin((2\lceil j/2\rceil-1)\pi/(2N))\ge j/N\);
the elementary sine concavity bound includes both ends of the list.
Every \(m\)-element subproduct is at least the product of the first \(m\).
Also \(N|Q^{-j}-1|/j\le2\pi\).
Thus for \(m>\delta_I N\),
\[
 |a_{N,m}|\le(2\pi)^mN^m/m!
                         \le(2\pi e/\delta_I)^m.
\]
Increasing \(C_I\) bounds every coefficient by \(C_I^m\).
On a small enough fixed disk, summing (23) gives \(O_I(N^{-1})\);
the remaining two geometric tails are exponentially small.
This proves (22) locally uniformly, not only for each fixed moment.

The limiting function is exactly
\[
 \frac1{1-cz}=\int_0^\infty e^{zs}\frac{e^{-s/c}}c\,ds
                  \quad(\operatorname{Re}z<1/c).
 \tag{24}
\]
This gives a nonzero analytic initializer and its explicit density
for one scaled physical operator. It does not replace the finite
functional by a positive measure on the full operator algebra,
or identify that half-line with the original geometric contour.

## 6. Consequence for fixed-degree formulations

The charges (6) and arrays in (11) are specified before \(R\) is
evaluated. They give exact linear observations of its true source,
with the full coherent contraction inside each observation.
The closed-family equations (13) have fixed Laurent degree and can
be retained as linear relations among auxiliary observations.
They neither impose new equations on independently summed internal
heights nor change the original bilinear Conway gluing maps.

Degree four for a variational energy is not a bound on the degree of
the original crossing in the physical \(E\): its nilpotent Euler sum
can have degree \(N-1\). The analytic initializer estimate (22) therefore
cannot be inserted through an arbitrary word without the required
uniform source bounds and its retained original observation.

In particular the known polynomial initializer angle (18) is not
an angle bound after an arbitrary short tangle. No result here
identifies the auxiliary labels with meridians, supplies the relative
cycle of a geometric saddle, or proves that \(Z_N(R)\) is nonzero.
The original quartic source problem and its selected geometric lower
estimate remain. All formulas hold when its scalar vanishes.

## Complete inputs and coverage

H and T give the actual continuants, physical tensors, nested frame,
finite product and signed word action. A proves the all-bottom original
marked seam and one-label closed family. The additions here are the
balanced charged seam at every last height, (11)'s two-label family,
and the matched full graph row with its initialized moments and
locally uniform analytic limit.
No novelty for finite geometric sums or norm inequalities is claimed.

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| H | [Height pairing and marked boundary](research_coideal_height_pairing_and_marked_boundary.md) | 543 | bed81fcb12b20d16d41c55b476b13d8d69b1fe79d0d0620c31230ba652b1d82f |
| T | [Exact crossing transport](research_coideal_crossing_orthogonality_transport.md) | 595 | 4555fecc6377077dbdc4cfb3afac50f09d180efc5659716bac8497319310114c |
| A | [Whole marked auxiliary-height period](research_coideal_auxiliary_height_word_period.md) | 390 | c5ee504593b83671f8185502eb14cfaa0213d30041ed9f909d5b005f2aacbe3a |

Only written algebra and text/hash operations were used. Earlier final
notes, public manuscripts and the progress ledger remain unchanged.

