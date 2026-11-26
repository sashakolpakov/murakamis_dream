# An exact seven-term recurrence for the physical inner three-source

Private exact-source proof, 8 November 2026. The physical values of the
complete inner three-trace satisfy a closed difference equation of
fixed order. Its forcing is an explicit constant at even levels and
zero at odd levels. The equation comes from the original full Hermite
algebra, so its endpoint conditions still include the required first
normals. A separate finite summation-by-parts formula records the exact
adjoint for the weights in the remaining outer observation.

No mathematical numerical evaluation or frozen-source edit is used.
Neither a discrete WKB estimate nor exponential cancellation of the
outer sum is asserted.

## 1. Original source and operators

Keep the original notation
\[
\begin{gathered}
 N\ge3,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad U=m-1,
 \quad M=\lceil N/2\rceil,\quad \theta=\pi/N,\quad q=e^{i\theta},\\
 \eta=(-1)^D,\quad \kappa=q^{D^2/2},\qquad
 P_N(z)=2T_N(z/2)+2,\qquad
 \mathcal A_N=\mathbb C[z]/(P_N),\\
 c_j=2\cos((2j+1)\theta),\quad
 s_j=2\sin(j\theta),\quad S_j=\prod_{\nu=1}^j s_\nu,\quad S_0=1,\\
 e_j(z)=S_j^{-2}\prod_{\nu<j}(c_\nu-z),\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f .
\end{gathered}                                                     \tag{1}
\]
Let \(T\) be the original turn, \(Te_j=e_{D-j}\), let \(R\)
be multiplication by the original crossing, and let \(Z\) be
multiplication by \(z\). In particular
\[
 T^2=I,\qquad R(c_j)=\kappa(-1)^j q^{j(j+1)} .
                                                                    \tag{2}
\]
The full kernel, complete-end input, and full inner output are
\[
\begin{split}
 K_N^{\rm ord}(z,w)&=\sum_{j=0}^D e_j(z)e_j(w),\\
 F_N(z)&=K_N^{\rm ord}(-2,z),\\
 Q_N^{\rm full}(w)&=\phi_N^{(z)}
       [R(z)^3F_N(z)K_N^{\rm ord}(z,w)]
                  =T(R^3F_N)(w).
\end{split}                                                       \tag{3}
\]
The last equality is in the original quotient, with its canonical
ordinary representative on the left. Its scalar is not changed.

Write \(\mathcal L=TZT\) and
\(\mathcal L_n=R^{-n}\mathcal L R^n\). The original
[current-free crossing transport, equations (6), (24), and (28)](research_current_free_aw_crossing_transport.md)
gives
\[
\begin{gathered}
 T\mathcal LT=Z,\qquad T\mathcal L_{-1}T=\mathcal L_1,\\
 \mathcal L_{n+1}+qZ\mathcal L_n+q^2\mathcal L_{n-1}
                         =8qI \qquad(n\in\mathbb Z).
\end{gathered}                                                     \tag{4}
\]
Products in (4), and below, are ordered operator products.
The same source proves the identities at coalescing physical
angles with their first normals, not just at distinct values.

## 2. The full-quotient equation and its parity forcing

Define the fixed-order operator
\[
\boxed{\quad
 \mathcal D_{3,N}
   =q^{-2}(\mathcal L^2-I)\mathcal L_1
       +q^{-3}\mathcal L Z-8q^{-2}\mathcal L
                         +(8q^{-1}+2)I .
\quad}                                                            \tag{5}
\]

**Theorem 1.** In the original full algebra,
\[
\boxed{\quad
 \mathcal D_{3,N}Q_N^{\rm full}
     =-\frac{\eta\kappa^3}{N^2}P_N(-2)\,1
     =:\mathfrak f_N\,1,\qquad
 \mathfrak f_N=
 \begin{cases}
 4\kappa^3/N^2,&N\ \text{even},\\
 0,&N\ \text{odd}.
 \end{cases}
\quad}                                                            \tag{6}
\]
As an ordinary polynomial identity there is a scalar \(\rho_N\)
such that
\[
 \mathcal D_{3,N}Q_N^{\rm full}(w)
                 =\mathfrak f_N+\rho_N P_N(w).
                                                                    \tag{7}
\]
No estimate or vanishing of \(\rho_N\) is needed for (6).
The term in (7) must be retained off the physical spectrum.

*Proof.* The original full-kernel defect,
[kernel difference theorem, equation (5)](research_edge_kernel_difference_and_endpoint_bound.md),
at its free value \(w=-2\), is
\[
              (\mathcal L+2)F_N
                      =-\frac{\eta}{N^2}P_N(-2)e_D .
                                                                    \tag{8}
\]
This is an ordinary polynomial identity with the complete-end
normalization. Conjugate its operator by \(TR^3\). Since
\[
 TR^3(\mathcal L+2)R^{-3}T
                  =T\mathcal L_{-3}T+2I,
                                                                    \tag{9}
\]
equation (3) yields the asserted equation with this conjugated
operator. To identify it explicitly, put
\(\widehat{\mathcal L}_n=T\mathcal L_nT\). Equations (4) give
\[
\begin{split}
 \widehat{\mathcal L}_{-2}
    &=8q^{-1}I-q^{-2}Z-q^{-1}\mathcal L\mathcal L_1,\\
 \widehat{\mathcal L}_{-3}
    &=8q^{-1}I-q^{-2}\mathcal L_1
                           -q^{-1}\mathcal L\widehat{\mathcal L}_{-2}\\
    &=q^{-2}(\mathcal L^2-I)\mathcal L_1
       +q^{-3}\mathcal L Z-8q^{-2}\mathcal L+8q^{-1}I .
\end{split}                                                       \tag{10}
\]
This proves (5),(9), including the order of \(\mathcal L Z\).

The complete-end socle identity is
\[
                   (z-c_0)e_D=0\quad\text{in }\mathcal A_N .
\]
Consequently \(R^3e_D=\kappa^3e_D\); derivatives of the crossing
do not create an additional term on this socle vector.
Since \(Te_D=1\), transporting the right side of (8) gives
(6). Finally
\[
                    P_N(-2)=2(-1)^N+2
\]
proves its stated parity cases.

The ordinary realization of \(\mathcal L\) preserves degree and
that of \(\mathcal L_1\) raises degree by at most one. Thus
the polynomial on the left of (7) has degree at most
\(D+1=N\). Its difference from \(\mathfrak f_N\) is divisible
by \(P_N\), by (6), proving (7). In particular
\(\rho_N=[w^N]\mathcal D_{3,N}Q_N^{\rm full}\).
\(\square\)

Equation (7) retains all endpoint data. At every double physical
node both the value and first ordinary derivative of its defect
vanish. At the odd simple node \(-2\) the value is the required
condition. Apparent poles of the angular operators are grouped
before these values or derivatives are taken, precisely as in
the current-free crossing theorem. No distinct-node replacement
of the full trace has been used.

## 3. The actual seven-term equation in the interior

Set
\[
 u_{j,N}=\pi-(2j+1)\theta,\qquad
                    q_{j,N}=Q_N^{\rm full}(c_j).
                                                                    \tag{11}
\]
The shortened second-edge output of the
[physical inner packet](research_mixed_next_inner_three_physical_outgoing_packet.md)
has exactly these same values for \(0\le j\le U\). This follows
from its literal kernel identity, not from an asymptotic comparison.

For interior indices use
\[
\begin{split}
 A_j&=\frac{s_{j+1}^4}{s_{2j+1}s_{2j+2}},&
 C_j&=\frac{s_j^4}{s_{2j}s_{2j+1}},&
 B_j&=c_0+A_j+C_j,\\
 (\mathbf Lf)_j&=B_jf_j-A_jf_{j+1}-C_jf_{j-1},\\
 (\mathbf L_1f)_j
       &=B_jf_j+q^{2j+2}A_jf_{j+1}
                            +q^{-2j}C_jf_{j-1},&
 (\mathbf Zf)_j&=c_jf_j .
\end{split}                                                       \tag{12}
\]
Indeed \(u_{j+1,N}=u_{j,N}-2\theta\),
\(qe^{-iu_{j,N}}=-q^{2j+2}\), and
\(qe^{iu_{j,N}}=-q^{-2j}\). Thus (12) is the original
angular operator and its \(n=1\) conjugate, with their exact phases.

Let \(\mathbf D_3\) be (5) with these sequence operators.
On \(3\le j\le U-3\), all its separate coefficients are regular,
and it has the exact form
\[
 (\mathbf D_3 f)_j=\sum_{r=-3}^{3}d_{j,r}f_{j+r}.
                                                                    \tag{13}
\]
Its two extreme coefficients are
\[
 d_{j,3}=q^{2j+4}A_jA_{j+1}A_{j+2},\qquad
 d_{j,-3}=q^{-2j+2}C_jC_{j-1}C_{j-2}.
                                                                    \tag{14}
\]
They are nonzero on this interior range. The other coefficients
are specified exactly by the ordered expression (5),(12).

**Corollary 2.** The actual shortened physical values satisfy
\[
                  \sum_{r=-3}^{3}d_{j,r}q_{j+r,N}
                                   =\mathfrak f_N,
                \qquad 3\le j\le U-3 .
                                                                    \tag{15}
\]
All seven values here are from the same original source and
the same level.

*Proof.* On this range each shift in (5) lands on an eligible
double physical node, with no coalescing coefficient pole.
Evaluate (6), then replace the full output values by their
identical shortened values from (11). The extreme coefficients
come only from \(q^{-2}\mathbf L^2\mathbf L_1\), which gives
(14) directly. \(\square\)

This passage does not extend (15), with separated singular
coefficients, to an endpoint. The full polynomial relation (7)
remains the endpoint statement. In particular the shortened
output has the same physical values as the full output but is
not asserted to have its first normals. The packet in the cited
source supplies initial asymptotic information only where
\(0<u_{j,N}\le\pi/2\), plus its separately handled complete
angle. It does not give all the boundary data for (15).

## 4. The exact adjoint for the remaining outer weights

The consumed original outer normal has coefficients
\[
 \beta_{j,N}=(-1)^{U+j}s_{2j+1}
          \frac{S_U^2}{S_{U-j}S_{U+j+1}},\qquad 0\le j\le U .
                                                                    \tag{16}
\]
Define the full observation weights
\[
 \mu_{j,N}=\beta_{j,N}R(c_j)^3
          =(-1)^U\kappa^3\omega_{j,N}q^{3j(j+1)},
                                                                    \tag{17}
\]
where the exact positive amplitudes, from
[the Casimir observation, equations (15)--(17)](research_mixed_next_three_outer_casimir_observation.md),
are
\[
 \omega_{j,N}=
 \begin{cases}
 s_{2j+1}/2,&N=2m,\\[1mm]
 s_{2j+1}s_{m-j}/\{4\cos^2(\theta/2)\},&N=2m+1 .
 \end{cases}
                                                                    \tag{18}
\]
Every \(\mu_{j,N}\) is nonzero. For all eligible \(i,j\),
\[
 \frac{\mu_{j,N}}{\mu_{i,N}}
       =\frac{\omega_{j,N}}{\omega_{i,N}}\,
                      q^{3\{j(j+1)-i(i+1)\}} .
                                                                    \tag{19}
\]
The cancellation of the two alternating signs in (17) is exact;
the quadratic crossing phase remains.

Here is a finite adjoint formula with all boundary terms.
Take an integer interval \(I=[a,b]\cap\mathbb Z\), with
\(6\le a\le b\le U-6\); empty ranges require no assertion.
Let \(f,h\) be sequences on its six-index neighborhood.
For \(i\in I\), define
\[
 (\mathbf D_3^\dagger h)_i
       =\sum_{r=-3}^{3}
          \frac{\mu_{i-r,N}}{\mu_{i,N}}\,
                         d_{i-r,r}h_{i-r}.
                                                                    \tag{20}
\]
This is a bilinear adjoint for the actual complex weights;
there is no conjugation or positivity assertion. Exact
reindexing gives
\[
\begin{split}
 \sum_{j\in I}\mu_{j,N}h_j(\mathbf D_3f)_j
  ={}&\sum_{i\in I}\mu_{i,N}(\mathbf D_3^\dagger h)_if_i
                             +\mathcal B_I(h,f),\\
 \mathcal B_I(h,f)
  ={}&\sum_{r=-3}^{3}
      \sum_{\substack{j\in I\\j+r\notin I}}
          \mu_{j,N}h_jd_{j,r}f_{j+r}\\
    &-\sum_{r=-3}^{3}
      \sum_{\substack{j\notin I\\j+r\in I}}
          \mu_{j,N}h_jd_{j,r}f_{j+r}.
\end{split}                                                       \tag{21}
\]
All sums in the last line use only \(|j-i|\le3\) with \(i\in I\).
Thus every boundary term belongs to one of the two fixed-width
endpoint neighborhoods. The bounds on \(a,b\) ensure that all
coefficient centers occurring in (21) lie in the regular
range of (13).

Putting \(f_j=q_{j,N}\) in (21) and using (15) gives
\[
 \sum_{i\in I}\mu_{i,N}(\mathbf D_3^\dagger h)_iq_{i,N}
   =\mathfrak f_N\sum_{j\in I}\mu_{j,N}h_j
                                -\mathcal B_I(h,q).
                                                                    \tag{22}
\]
This relation keeps the errors as a sequence. For example,
if an approximate sequence \(p_j\) has residual
\(\epsilon_j=(\mathbf D_3p)_j-\mathfrak f_N\), then
the exact error \(r_j=q_{j,N}-p_j\) obeys
\[
 \sum_{i\in I}\mu_{i,N}(\mathbf D_3^\dagger h)_ir_i
       =-\sum_{j\in I}\mu_{j,N}h_j\epsilon_j
                                  -\mathcal B_I(h,r).
                                                                    \tag{23}
\]
Neither the residual term nor either boundary contribution
has been removed.

## 5. What would make this recurrence useful for suppression

The exact unresolved observation is
\[
 \mathcal L_N(H_N)
        =\sum_{j=0}^{U}\mu_{j,N}H_N(c_j,Z_*)q_{j,N}.
                                                                    \tag{24}
\]
It retains the outside scalar
\((-q)^M/(\kappa^2N)\) in the original transfer. Equations
(20)--(23) specify an actual adjoint problem for its
interior portion: one would need a controlled solution of
\(\mathbf D_3^\dagger h=H_N(c_\bullet,Z_*)\), together
with the two endpoint contributions and the remaining
physical indices.

The physical packet supplies
\[
 q_{j,N}=C_{N,3}N^{-3/2}\mathcal A(u_{j,N})
          e^{NS(u_{j,N})}(1+O(N^{-1}))
                                                                    \tag{25}
\]
on its stated node range. Equations (15),(23) are additional
exact constraints on its error sequence. They do not by
themselves provide an exponentially accurate WKB expansion,
a bounded adjoint inverse, or a bound for the initial and
terminal error data. In particular the \(O(N^{-1})\) error
in (25) is not substituted into (24) after cancellation.

The original operator source already exhibits exponential
inverse costs for related forced terminal equations. Its
fixed-strip forward bounds therefore cannot be used as a
subexponential inverse estimate here. Likewise (17)--(18)
do not make the observation a positive trace.

The new conclusion is the closed actual-source recurrence
(6),(15), its explicit parity forcing and off-grid defect,
and the exact weighted adjoint (21)--(23). A bound for the
coherent observation at the required budget \(B_f\), and
hence the full transfer conclusion, remains to be proved.
