# A shifted retained chart and its diagonal residue currents

Research deduction, 7 November 2026. Shifting the outgoing
argument by one period inside the retained polynomial converts
the difference of two upper retained aliases into an outgoing
lower-alias factor. The shifted chart is meromorphic on part of
the relevant retained rectangle. This note retains its diagonal
poles and gives the exact residue correction to the four-current
formula.

No bound for the new residue sum or unpenalized shifted current
is asserted. In particular the outgoing alias factor alone does
not prove an exponential source gap.

## 1. The same literal source in two retained charts

Use the actual references and finite factors of
[the one-horizontal-integral reduction](research_mixed_fourier_right_cap_main_reduction.md).
Fix an outgoing point
\[
 q=z+i h_q,\qquad 9/20\le z<1,\qquad
 -.102\le h_q\le-.001 .
 \tag{1}
\]
The incoming parameter \(a\), its type \(\eta\), and its finite
halfweight are unchanged. All formulas below retain the same
global cardinal \(\widehat f_N(q;y)\), with its original scalar.

Let \(L_N=\lceil N/8\rceil\), \(M_N=\lceil N/2\rceil-1\),
and use the original half-grid cuts \(\sigma_\pm\).
Write the unshifted central row as
\[
 T_N(s,q)=e^{2\pi iNas}\Pi_N(s+a)E_N(a)
          \Pi_N(s+q)E_N(q)E_N(s)^3\widehat f_N(q;y),
 \tag{2}
\]
and define the shifted meromorphic row
\[
 \widetilde T_N(s,q)=e^{2\pi iNas}\Pi_N(s+a)E_N(a)
          \Pi_N(s+q-1)E_N(q-1)E_N(s)^3\widehat f_N(q;y).
 \tag{3}
\]
The continuation of the shifted numerator is specified in
Section 2; it is not assumed holomorphic across its poles.
Since \(\Im q<0\), the factor \(E_N(q-1)\) itself is
holomorphic and nonzero on this parameter family.

At each physical retained \(s=j/N\), exact recurrence gives
\[
 \widetilde T_N(j/N,q)=T_N(j/N,q)
   =\frac{X^{-j}p_j(X)p_j(e^{-2\pi iq})}{P_j^3}
                                     \widehat f_N(q;y).
 \tag{4}
\]
Here \(p_j(e^{-2\pi i(q-1)})=p_j(e^{-2\pi iq})\) is
literal polynomial periodicity. Formula (4) is used at
physical retained indices; it does not identify the two
off-grid functions.

Put
\[
                  Z_q=e^{-2\pi iNq},\qquad
                  \mathcal A_q=\frac{Z_q}{1-Z_q}.
 \tag{5}
\]
The denominator is nonzero because \(|Z_q|<1\).
The exact factorial period identity gives the meromorphic
identity
\[
 \begin{split}
 T_N(s,q)
  &=\widetilde T_N(s,q)
          \frac{1-e^{-2\pi iN(s+q)}}{1-e^{-2\pi iNq}},\\
 T_N(s,q)-\widetilde T_N(s,q)
  &=\mathcal A_q(1-e^{-2\pi iNs})\widetilde T_N(s,q).
 \end{split}
 \tag{6}
\]
Both sides in the first line extend meromorphically through
the displayed zeros. The identity is not used to divide a
vanishing numerator at a pole.

## 2. Every shifted diagonal pole and its residue

The original factorial period relation is
\[
                 \Pi_N(w+1)=(1-e^{-2\pi iNw})\Pi_N(w).
 \tag{7}
\]
On \(-1<\Re w<1\), use (7) to continue \(\Pi_N(w)\)
meromorphically from its original domain. Its negative
poles in that strip are exactly
\[
 w=-k/N,\qquad 1\le k<N,
 \qquad
              \operatorname*{Res}_{w=-k/N}\Pi_N(w)
                          =\frac{P_{N-k}}{2\pi iN}.
 \tag{8}
\]
They are simple. Indeed the numerator \(\Pi_N(w+1)\)
has the nonzero value \(P_{N-k}\), and the derivative
of \(1-e^{-2\pi iNw}\) is \(2\pi iN\) there.
The zeros of that denominator at \(0\le\Re w<1\)
are removable: the numerator has the matching original
positive-support zero. Thus no additional pole is introduced.

On the complete retained rectangle
\[
 \sigma_-\le\Re s\le\sigma_+,\qquad
                     -1/5\le\Im s\le5/4,
 \tag{9}
\]
the shifted numerator argument \(s+q-1\) lies in the
strip just discussed, for all sufficiently large \(N\).
All other \(s\)-dependent factors in (3) are regular.
The only possible poles are therefore
\[
 s_k(q)=1-q-k/N,\qquad 1\le k<N.
 \tag{10}
\]
Their common height is \(-h_q\in[.001,.102]\), above
the zero-mode height \(h_s<0\) and below \(5/4\).
For poles strictly between the real cuts, define
\[
 \begin{split}
 \mathcal K_N(q)&=\{k:1\le k<N,\
                      \sigma_-<1-z-k/N<\sigma_+\},\\
 \mathcal B_{k,N}(q)&=
 e^{2\pi iNa s_k(q)}\Pi_N(s_k(q)+a)E_N(a)
      E_N(s_k(q))^3 P_{N-k} E_N(q-1)\widehat f_N(q;y).
 \end{split}
 \tag{11}
\]
Then
\[
       \operatorname*{Res}_{s=s_k(q)}\widetilde T_N(s,q)
                            =\frac{\mathcal B_{k,N}(q)}{2\pi iN}.
 \tag{12}
\]
Every finite scalar and original cardinal coefficient is
retained in this formula. A zero of another factor can
make the residue vanish, but no division by such a factor
is made.

## 3. The corrected four-current formula

For a meromorphic function \(F\) with the poles (10), define
\(\mathcal Z_N[F],\mathcal L_N[F],\mathcal U_N[F],
\mathcal V_N[F]\) by the original four-current formulas:
\[
 \begin{split}
 \mathcal Z_N[F]&=N\int_{\sigma_-}^{\sigma_+}F(u+i h_s)\,du,\\
 \mathcal L_N[F]&=N\int_{\sigma_-}^{\sigma_+}F(u-i/5)
             \frac{e^{-2\pi iN(u-i/5)}}{1-e^{-2\pi iN(u-i/5)}}\,du,\\
 \mathcal U_N[F]&=N\int_{\sigma_-}^{\sigma_+}F(u+5i/4)
             \frac{e^{2\pi iN(u+5i/4)}}{1-e^{2\pi iN(u+5i/4)}}\,du,\\
 \mathcal V_N[F]&=iN\int_{-1/5}^{5/4}w_{N,h_s}(v)
                       [F(\sigma_++iv)-F(\sigma_-+iv)]\,dv .
 \end{split}
 \tag{13}
\]
For the moment assume no pole lies on a vertical side.
All poles are above \(h_s\).

**Lemma 1.** The physical retained sum satisfies
\[
 \sum_{j=L_N}^{M_N}F(j/N)
  =\mathcal Z_N[F]+\mathcal L_N[F]
      +\mathcal U_N[F]+\mathcal V_N[F]
     +2\pi iN\sum_k
       \frac{e^{2\pi iNs_k}}{1-e^{2\pi iNs_k}}
                     \operatorname*{Res}_{s=s_k}F(s).
 \tag{14}
\]

To check the correction and its sign, the exact cotangent
rectangle has total residue
\[
 \frac1{2\pi i}\int_{\partial R}
           F(s)\pi N\cot(\pi Ns)\,ds
   =\sum_j F(j/N)
           +\sum_k\pi N\cot(\pi Ns_k)\operatorname*{Res}_{s_k}F.
 \tag{15}
\]
When its constant top and bottom kernel pieces are moved
to the zero-mode height, the upper region encloses the
source poles. Cauchy's formula contributes
\(-\pi iN\sum_k\operatorname*{Res}_{s_k}F\) to the
four-current regrouping of the left side of (15).
Thus the physical sum is the four-current expression
minus
\(\pi N\sum_k(\cot(\pi Ns_k)+i)\operatorname*{Res}F\).
Since
\[
 \cot(\pi Ns_k)+i
            =-\frac{2i e^{2\pi iNs_k}}{1-e^{2\pi iNs_k}},
 \tag{16}
\]
this is exactly (14). This derivation also shows why the
bare cotangent residue alone would give the wrong correction:
the zero-mode height change crosses the same source poles.

For (10), one has \(e^{2\pi iNs_k}=Z_q\), independently
of \(k\). Substituting (12) into (14), and then using
the physical equality (4), gives the exact formula
\[
 \boxed{\quad
 \sum_{j=L_N}^{M_N}T_N(j/N,q)
  =\mathcal Z_N[\widetilde T_N]
    +\mathcal L_N[\widetilde T_N]
    +\mathcal U_N[\widetilde T_N]
    +\mathcal V_N[\widetilde T_N]
            +\mathcal A_q\sum_{k\in\mathcal K_N(q)}
                              \mathcal B_{k,N}(q).
 \quad}
 \tag{17}
\]
The extra term retains the outgoing lower-alias factor
\(\mathcal A_q\), with the explicit finite residue sum.
No physical support restriction is imposed off-grid.

There is also an exact identity for the upper horizontal
current alone. On that contour there are no shifted poles,
and
\[
 (1-e^{-2\pi iNs})
       \frac{e^{2\pi iNs}}{1-e^{2\pi iNs}}=-1 .
 \]
Equation (6) consequently gives
\[
 \boxed{\quad
 \mathcal U_N[T_N(\,\cdot\,,q)]
   =\mathcal U_N[\widetilde T_N(\,\cdot\,,q)]
       -\mathcal A_q N\int_{\sigma_-}^{\sigma_+}
                          \widetilde T_N(u+5i/4,q)\,du .
 \quad}
 \tag{18}
\]
The new integral in (18) is unpenalized in the retained
variable. Its outgoing factor must be kept; neither
factor is separately declared small.

## 4. Integrating across the diagonal side crossings

As \(z\) varies on a closed outgoing subinterval, a pole
crosses a retained side only at the finitely many points
\[
                    z=1-\sigma_\pm-k/N.
 \tag{19}
\]
On each complementary open subinterval, (17) holds with
the indicated fixed pole inventory. At a crossing, the
shifted vertical integral and the residue count change
together. Their combination remains the same analytic
physical sum (4). One may take its one-sided limit,
or use matched small contour indentations and retain
their residue contribution before passing to the limit.

There is also a direct integrated interpretation without
discarding any point contribution. Near a side crossing,
the only local singularity of the shifted two-real-variable
vertical integrand is a smooth coefficient times
\[
           \frac1{(z-z_0)+i(v+h_q)}.
 \tag{20}
\]
It is locally absolutely integrable in the \((z,v)\) plane.
The fixed cotangent weights are regular there because
\(-h_q>0\). Hence the double vertical current is well
defined by ordinary integration; its inner integral may
be defined arbitrarily at the finitely many exceptional
\(z\). The residue sum in (17) is a bounded piecewise
continuous function at fixed \(N\), with the prescribed
inventory (11).

Multiplying (17) by the original outgoing coefficient
\(+N\) and integrating over any such closed outgoing
subinterval therefore gives an exact current identity.
It includes the integrated diagonal residue current
\[
       N\int \mathcal A_{z+i h_q}
          \sum_{k\in\mathcal K_N(z+i h_q)}
                    \mathcal B_{k,N}(z+i h_q)\,dz .
 \tag{21}
\]
The sign, cardinal scalar and all powers of \(N\) in
(21) follow from (12)--(17); no new normalization is used.
The physical low retained rows \(j<L_N\) remain a
separate exact source if this identity is applied to
the complete low-index cap.

## 5. What this identity changes and what it does not prove

The upper retained correction in the unshifted chart can
grow at large positive height. Equation (18) is compatible
with that fact: its new unpenalized shifted top current
can carry the same growth. It is not removed by assigning
an independent outgoing support condition.

The exact improvement is that the wrap difference and
every diagonal residue occur with the same specified
outgoing lower-alias factor. This supplies a coherent
current identity for a possible coupled contour estimate.
An estimate must still retain the unpenalized current
in (18), the residue current (21), and any contour
connectors it creates. No calibrated bound or full
right-cap conclusion is inferred here.
