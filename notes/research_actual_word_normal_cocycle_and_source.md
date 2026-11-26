# Actual braid words, the normal cocycle, and the original source

Private written proof, 19 November 2026. Author-final for independent review.

The first normal layer of the actual root braid algebra has an
explicit generator transport. In a common frame that makes the
remaining lowering operator constant, every internal crossing has
zero quotient-normal class. The boundary crossing has a finite
formula from its actual capped prefix coefficients. The original
closing of any word is then a sum of Levi traces, diagonal normal
terms, and specified quadratic couplings of off-diagonal blocks.

This is a finite source theorem. It does not replace the closing
by a positive norm or prove a geometric coefficient is nonzero.
The complete directs are F, the reciprocal flag classification;
C, the actual prefix Ward equations; and R, the actual reduced
braid representation and its source. All additional normal,
frame, generator, and word calculations are proved below.

## 1. The actual root algebra and its normal derivation

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
and \(m=r+1\ge2\). Keep the quantum root fixed and put
\(M=e^\mu\), \(x=-M/q\). Write
\(f_n=\prod_{j=1}^n(1-Q^j)\), \(f_0=1\), and
\({t\brack n}_Q=f_t/(f_nf_{t-n})\) for \(0\le n\le t<N\).
On the remaining tensor \(U\), write
\[
 K(M)=M^rK_0,\quad K_0^N=\varepsilon I,\quad
 \varepsilon=(-1)^{(N+1)r},\qquad
 \mathcal A=\operatorname{End}_{K_0}(U).
 \tag{1}
\]
For a literal braid word \(\beta\), including its crossing scalars,
let
\[
 \rho_\mu(\beta)=p_0S_m(M)^{-1}W_\beta(M)i_0.
 \tag{2}
\]
R proves that this is an actual holomorphic group representation
into \(\mathcal A^\times\). All indices stay in \(0,\ldots,d\).

F identifies the entire actual root intertwiner algebra with
\[
 \mathcal T=V\oplus(\mathcal A/V),\qquad
 (b,[c])(b',[c'])=(bb',[bc'+cb']),
 \tag{3}
\]
where \(V\) is the root prefix image. The coordinates of a root
intertwiner lifted analytically to \(W(\mu)\) are the constant
coefficient and the first coefficient modulo \(V\) of its actual
reduced family. They do not depend on the lift: the difference of
two lifts is \(\mu T(\mu)\), whose reduced first coefficient lies
in \(V\). Write these coordinates as \(\pi(W)\) and \(\nu(W)\).
Thus the exact normal map satisfies
\[
 \nu(WZ)=\pi(W)\nu(Z)+\nu(W)\pi(Z).
 \tag{4}
\]
This is a derivation relative to the root reduction, not a
derivation determined by its value \(\pi(W)\) alone.

For actual braid words put \(b_\beta=\rho_0(\beta)\) and
\[
 c_\beta=[\rho'_0(\beta)b_\beta^{-1}]\in\mathcal A/V.
 \tag{5}
\]
Since \(b_\beta^{\pm1}\in V\), conjugation acts on this quotient.
The ordinary product rule gives
\[
 \boxed{\quad
 c_{\beta\gamma}=c_\beta+\operatorname{Ad}(b_\beta)c_\gamma,
 \qquad c_{\beta^{-1}}=-\operatorname{Ad}(b_\beta^{-1})c_\beta.
 \quad}\tag{6}
\]
It is a cocycle on the actual root braid operators, or equivalently
on braid words through their full root operators. It need not
descend to the reduced root matrix \(b_\beta\) alone. The lost
square-zero layer in (3) is precisely the datum that would be
discarded by that stronger assertion.

## 2. A common moving frame, with every connection term

There is an analytic \(K_0\)-preserving matrix \(G(\mu)\), with
\(G(0)=I\), such that
\[
                   G(\mu)^{-1}E_r(M)G(\mu)=E_r(1)=:E.
 \tag{7}
\]
Here is a finite construction. Split the first remaining head
from the rest. The columns
\(E_r(M)^a(w_d\otimes v)\), \(0\le a\le d\), in a fixed
remaining occupation basis \(v\), form a matrix \(T(M)\).
Its least first-head row is \(d-a\), with invertible coefficient
\((e_d\cdots e_{d-a+1})K_{\rm rest}^a\), where
\(e_j=MQ^{-j}-M^{-1}\). This gives an analytic triangular basis
near \(M=1\). For one remaining head use the same construction
with empty rest. Finite root quantum-binomial expansion and the
forced head endpoints give \(E_r(M)^N=0\). Thus \(T(M)\) makes
\(E_r(M)\) the same length-\(N\) Jordan shift for every \(M\).
Take \(G(M)=T(M)T(1)^{-1}\). Every column has a fixed \(K_0\)
weight, so \([G,K_0]=0\), proving (7) with the stated normalization.

Set
\[
 \widehat\rho_\mu(\beta)=G^{-1}\rho_\mu(\beta)G,
 \qquad \Gamma=G'(0),\qquad
 h_\beta=\widehat\rho'_0(\beta)
                   =\rho'_0(\beta)+[b_\beta,\Gamma].
 \tag{8}
\]
The quotient-normal class is therefore changed by the explicit
inner derivation \([b_\beta,\Gamma]\bmod V\). Its logarithmic
version changes by the coboundary
\[
      \widehat c_\beta=c_\beta+
                       [\operatorname{Ad}(b_\beta)\Gamma-\Gamma].
 \tag{9}
\]
No meridian derivative of the frame has been suppressed.

The flattened quotient-normal class is independent of the choice
of frame satisfying (7) and \(G(0)=I\). Indeed two such frames
differ by a matrix commuting with \(E\) and \(K_0\); its derivative
at zero commutes with both arrows in F's reciprocal complexes.
F's classification puts that derivative in \(V\), so the change
in (9) is zero in \(\mathcal A/V\).

The source is invariant under this moving frame for the entire
meridian germ. R's exact source matrix is central in \(\mathcal A\):
with \(D_N(z)=(z^N-z^{-N})/(z-z^{-1})\),
\[
 D_\mu=\frac{D_N(M)}{D_N(MK(M))},\qquad
 \Phi_0(W_\beta(M))=\operatorname{Tr}(D_\mu\rho_\mu(\beta))
                  =\operatorname{Tr}(D_\mu\widehat\rho_\mu(\beta)).
 \tag{10}
\]
This equality is made before taking a finite part. In particular
the polar-source trace of the commutator in (8) is exactly zero,
not an estimate of a pointwise coherent kernel.

For an internal original generator \(\sigma_i^{\pm1}\), \(i\ge2\),
R identifies its reduced matrix with the physical crossing on the
remaining heads. It commutes with \(E_r(M)\) for all \(M\).
Consequently its flattened matrix commutes with \(E\) and \(K_0\)
for all \(\mu\). F then puts it in the fixed algebra \(V\)
throughout the germ, so
\[
       [h_{\sigma_i^{\pm1}}]=0\quad\hbox{in }\mathcal A/V,
                                      \qquad i\ge2.
 \tag{11}
\]
This statement concerns internal generators only. The initialized
boundary generator has an explicit normal adapter below.

## 3. The whole-meridian boundary coefficients

Write C's full prefix expansion of an actual word as
\[
 S_m^{-1}W_\beta S_m=\sum_{n=0}^dF_1^n\otimes B_n^\beta,
                         \qquad B_0^\beta=\rho_\mu(\beta).
 \tag{12}
\]
Let \(L_2\) be the literal lowering shift on the first remaining
head, with its zero bottom arrow. The positive first crossing has
the exact whole-meridian identity
\[
 \boxed{\qquad
 B_n^{\sigma_1}(M)=\frac{x^{-n}}{f_n}
                          \rho_\mu(\sigma_1)L_2^n,
                          \qquad 0\le n\le d.
 \qquad}\tag{13}
\]
To verify it, R's zero-transfer input row is
\(R_1(w_0\otimes w_b\otimes v)=\kappa(M)x^{-b}
w_b\otimes w_0\otimes v\). Put
\(c_j=(-1)^jQ^{j(j-1)/2}\). The term of \(S_m^{-1}\) returning
this first-head occupation to \(n\) has \(j=b-n\). Therefore,
for \(b\ge n\),
\[
 B_n^{\sigma_1}(w_b\otimes v)
   =\frac{\kappa c_{b-n}x^{-2b+n}}{f_nf_{b-n}}
                         F_r^{b-n}(w_0\otimes v).
 \tag{14}
\]
It is zero for \(b<n\). R's formula for \(\rho(\sigma_1)\)
applied to \(L_2^n(w_b\otimes v)\) is precisely (14), proving
(13), including \(\kappa\), every physical cap, and every fixed-
quantum meridian derivative. In particular no upper transfer sum
or root-only identity has been differentiated.

## 4. Division-free normal arrow defects

Fix a nonself pair \(\{\chi,\chi^{-1}\}\), and choose the unique
\(1\le s<N\) with \(Q^s=\chi^2\). Set
\[
       A=E^s:U_{\chi^{-1}}\to U_\chi,
       B=E^{N-s}:U_\chi\to U_{\chi^{-1}}.
 \tag{15}
\]
These are F's actual exact-complex arrows. In the common frame
(7) they remain constant throughout the meridian germ. The actual
weights are \(M^r\chi\) and \(M^r\chi^{-1}\); they need not be
reciprocal away from zero.

For a fixed root weight \(\lambda_0\), the total prefix weight
\(x(M)M^r\lambda_0\) has tail weight
\(M^rQ^n\lambda_0\) in first-head row \(n\). Put
\(\widehat E'=(I\otimes G^{-1})S_m^{-1}E_\Sigma S_m(I\otimes G)\).
C's transformed lowering row gives, for \(0\le n\le t<N\),
\[
 p_0(\widehat E')^t i_n
       =c_{t,n}(\lambda_0;\mu)E^{t-n},\quad
 c_{t,n}=Q^{n(n-1)/2}{t\brack n}_Q
       \prod_{j=t}^{t+n-1}
          (M^m\lambda_0-M^{-m}Q^{-j}\lambda_0^{-1}).
 \tag{16}
\]
It is zero for \(n>t\), and \(c_{t,0}=1\). The same first-step
recurrence as in F proves (16): a tail step replaces
\(\lambda_0\) by \(Q\lambda_0\), while a first-head lowering
step contributes
\(M^m\lambda_0-M^{-m}Q^{-n}\lambda_0^{-1}\).
The two finite Gaussian Pascal identities complete the induction.
Only indices below \(N\) occur.

If \(\lambda_0^2=Q^{-t}\), the first factor of every nonempty
product in (16) vanishes at zero. Its derivative is
\(2m\lambda_0\). The remaining factors are
\(\lambda_0(1-Q^{-j})\), \(1\le j<n\), so exactly
\[
 \boxed{\qquad
 \partial_\mu c_{t,n}|_0
      =2m(-1)^{n-1}\lambda_0^n{t\brack n}_Q f_{n-1}
      =:\omega_{t,n}(\lambda_0),\qquad 1\le n\le t.
 \qquad}\tag{17}
\]
The phase \(Q^{n(n-1)/2}\) cancels the negative-power product;
there is no missing Cartan or factorial scalar.

Put \(\widehat B_n^\beta=G^{-1}B_n^\beta G\). Commuting the whole
word with \(\widehat E'\), and retaining all columns in (16), gives
\[
 \widehat\rho_{\mu,Q^t\lambda_0}(\beta)E^t
       -E^t\widehat\rho_{\mu,\lambda_0}(\beta)
   =\sum_{n=1}^t f_nc_{t,n}E^{t-n}
                     \widehat B_n^\beta|_{U_{\lambda_0}}.
 \tag{18}
\]
At resonance, differentiating has no derivative of the right-hand
matrix factors: each scalar \(c_{t,n}(0)\) is zero. Also \(G(0)=I\).
Thus the actual normal defect is
\[
 \boxed{\qquad
 \mathfrak D_t^\beta
 :=h_{\beta,Q^t\lambda_0}E^t-E^th_{\beta,\lambda_0}
   =\sum_{n=1}^t f_n\omega_{t,n}(\lambda_0)
                          E^{t-n}B_n^\beta(0).
 \qquad}\tag{19}
\]
Use \((\lambda_0,t)=(\chi^{-1},s)\) for \(\mathfrak D_A\),
and \((\chi,N-s)\) for \(\mathfrak D_B\). For the positive
boundary generator (13) makes (19) completely explicit:
\[
 \mathfrak D_t^{\sigma_1}
   =\sum_{n=1}^t\omega_{t,n}(\lambda_0)x_0^{-n}
                        E^{t-n}b_{\sigma_1}L_2^n,
                     \qquad x_0=-q^{-1}.
 \tag{20}
\]
All operators in (20) are the original root matrices. Displaying
them in flag bases conjugates every factor by those same fixed
bases; it does not replace \(L_2\) by a newly normalized shift.

Let \(X_\beta=b_\beta|_{U_\chi}\),
\(Y_\beta=b_\beta|_{U_{\chi^{-1}}}\). The product rule and the
root arrow intertwinings give
\[
 \mathfrak D_A^{\beta\gamma}
    =X_\beta\mathfrak D_A^\gamma+
                        \mathfrak D_A^\beta Y_\gamma,
 \qquad
 \mathfrak D_A^{\beta^{-1}}
    =-X_\beta^{-1}\mathfrak D_A^\beta Y_\beta^{-1}.
 \tag{21}
\]
The reverse arrow has the same formulas with \(X,Y\) interchanged.
This supplies the negative boundary generator with the actual
inverse and its scalar; no inverse-crossing approximation is used.

## 5. The normal class in the physical flag blocks

Choose F's fixed complements, so the pair spaces have dimensions
\((k,l)\) and \((l,k)\), and the root word has the form
\[
 X_\beta=\begin{pmatrix}a_\beta&b_\beta^{\rm off}\\0&d_\beta\end{pmatrix},
 \qquad
 Y_\beta=\begin{pmatrix}d_\beta&f_\beta\\0&a_\beta\end{pmatrix}.
 \tag{22}
\]
The complements identify \(A\) and \(B\) with their identity
arrows as in F. Write the flattened first normal on the pair as
\((C_\beta,D_\beta)\), and define
\[
 \alpha_\beta=C_{11}-D_{22},\quad
 \delta_\beta=C_{22}-D_{11},\quad
 p_\beta=C_{21},\quad q_\beta=D_{21}.
 \tag{23}
\]
These are exactly its quotient class in \(\mathcal A/V\).
Direct multiplication by the two arrows gives
\[
 \mathfrak D_A^\beta=
   \begin{pmatrix}-q_\beta&\alpha_\beta\\0&p_\beta\end{pmatrix},
 \qquad
 \mathfrak D_B^\beta=
   \begin{pmatrix}-p_\beta&-\delta_\beta\\0&q_\beta\end{pmatrix}.
 \tag{24}
\]
Consequently (19)--(21) determine the entire actual quotient-normal
class, not just its closing trace. Internal generators have all
four blocks in (23) equal to zero, by (11).

The common crossing scalar is still included in every root matrix
in (20),(22). A logarithmic derivative of a scalar multiple of a
generator adds a scalar multiple of \(b_\beta\), which lies in
\(V\), so it has zero quotient-normal class. This observation
does not remove the scalar's root value. Nor does it remove its
derivative when differentiating the whole closed source rather
than computing its root value.

## 6. The exact closing of an arbitrary signed word

Write the literal word as \(\beta=g_L\cdots g_1\), with each
letter an actual signed generator. Use (22),(23) for each letter,
and write its diagonal blocks as \(a_i,d_i\) and off-diagonal
blocks as \(b_i^{\rm off},f_i\). For each \(i\), let
\[
       \gamma_i=g_{i-1}\cdots g_1g_L\cdots g_{i+1}.
 \tag{25}
\]
Its two root blocks are denoted by
\[
 X_{\gamma_i}=\begin{pmatrix}A_i&B_i\\0&D_i^{\rm c}\end{pmatrix},
 \qquad
 Y_{\gamma_i}=\begin{pmatrix}D_i^{\rm c}&F_i\\0&A_i\end{pmatrix}.
 \tag{26}
\]
An empty product is the identity. Put
\(a_\chi=(\chi-\chi^{-1})/(2\varepsilon m)\). Then the
original source contribution of this whole physical pair is
\[
 \boxed{\begin{aligned}
 \Phi_{\mathfrak o}(W_\beta(1))={}&
 \frac{\chi+\chi^{-1}}{\varepsilon}
     \left[\operatorname{Tr}(a_L\cdots a_1)
                       +\operatorname{Tr}(d_L\cdots d_1)\right]\\
 &+a_\chi\sum_{i=1}^L
   \left[\operatorname{Tr}(\alpha_iA_i)
        +\operatorname{Tr}(\delta_iD_i^{\rm c})
        +\operatorname{Tr}(p_iB_i)-\operatorname{Tr}(q_iF_i)\right].
 \end{aligned}}\tag{27}
\]
Every trace is on its indicated rectangular product's square
space. To prove (27), the actual first derivative of the matrix
product is a sum with one \((C_i,D_i)\) insertion. Cyclicity of
each ordinary block trace changes its complementary factors to
(25). Expanding
\(\operatorname{Tr}(C_iX_{\gamma_i}-D_iY_{\gamma_i})\) gives
exactly its four displayed terms. F's original source formula
then gives (27), including \(a_\chi\) and the Levi coefficient.

Each \(B_i,F_i\) in (26) is a sum with exactly one root
off-diagonal letter. For an ordered upper-triangular product this
follows by choosing the unique step from its lower block to its
upper block. Thus the last two terms in (27) are the actual
quadratic couplings between a root off-diagonal and a normal
off-diagonal. Trace removes either one in isolation; it does not
remove their products. No adjoint, complex conjugation, or norm
has replaced these bilinear contractions.

For a self weight \(\chi=\pm1\), the source contribution is
\(\chi\operatorname{Tr}(b_\beta|_{U_\chi})/\varepsilon\), counted
once. Summing these and (27) over all inversion orbits gives the
entire original pointed source. Separately prescribed exterior
scalar lines multiply that full result with their actual values.
They retain their product-rule derivatives on the meridian germ.
Equation (27) computes the original root value from the reduced
first normal. For a fixed full root operator, the full reduced
first derivative is lift-dependent,
although its quotient class is not. A derivative of the original
closed source generally also needs the reduced second coefficient
against the simple pole in (10); no such extra jet is discarded
or supplied by the root formula (27).

## 7. One boundary occurrence and the exact remaining duty

Suppose a word has a single \(\sigma_1^{\epsilon}\),
\(\epsilon=\pm1\), and all other letters are internal. R's
cyclic source identity permits rotating it to
\(\sigma_1^{\epsilon}\eta\), with \(\eta\) internal. The same
cyclicity holds in each paired block since \(D_\mu\) is a scalar
there on each weight. By (11), only the boundary letter remains
in the normal sum of (27). If the internal root blocks are
\(a_\eta,d_\eta,b_\eta^{\rm off},f_\eta\), that normal term is
\[
 a_\chi\left[
   \operatorname{Tr}(\alpha_\epsilon a_\eta)
  +\operatorname{Tr}(\delta_\epsilon d_\eta)
  +\operatorname{Tr}(p_\epsilon b_\eta^{\rm off})
  -\operatorname{Tr}(q_\epsilon f_\eta)\right].
 \tag{28}
\]
The boundary covector is specified by the finite positive formula
(20),(24) or the exact inverse law (21). All extensive internal
spectators remain in the actual root word in (28).

For the positive left stabilization this is consistent with an
independent whole-meridian source contraction. If
\(W_\eta=I\otimes W_{\rm old}\), R's zero-transfer row and the
highest cut force the new first and old first occupations both to
zero. The retained pivotal factor there is \(x^{1-N}\). Hence
\[
 \Phi_0(R_1(I\otimes W_{\rm old}))
                  =\kappa(M)x^{1-N}\Phi_0(W_{\rm old}).
 \tag{29}
\]
The actual positive zero-framing compensation cancels this same
scalar, as in R. Equation (29) retains its true meridian
derivative; it is not a new nonzero-source theorem.

The result completes the finite normal transport of actual signed
words and their prescribed closing. It reduces a one-boundary
presentation to an explicit boundary covector against an actual
internal root representation, rather than an unspecified normal
matrix. It supplies no analytic lower bound for that contraction,
no positive Levi metric, and no selected geometric coefficient.
The remaining coefficient and relative-cycle estimates cannot be
deduced from radical nilpotence or invertibility of the word.

## Complete direct-source pins

* F: notes/research_reciprocal_chain_flags_and_root_radical.md,
  428 lines, SHA256
  7589bb0f796a874608b9e558aac1f78699884f0003da4a73ba52778c1edba66e.
* C: notes/research_prefix_commutant_and_pointed_normal_functional.md,
  549 lines, SHA256
  b4fb801a1482316aebb4799f1d0b80d5b43ced39138d903c04cfde811ca166b0.
* R: notes/research_actual_reduced_braid_source.md,
  330 lines, SHA256
  9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.

All three complete directs were freshly whole-read nontruncated
in this author sequence. The entire matching final was freshly
read back nontruncated, every used implication checked, and all
four pins renewed before freezing. Independent matching review
and parent adoption remain separate. Only written mathematics
and text/hash operations were used. Frozen and public files were unchanged.
