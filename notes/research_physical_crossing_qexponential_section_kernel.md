# The crossing kernel for a finite geometric series

Private written proof, 19 November 2026.

The factorial donor frame turns the physical finite geometric series
\(\sum_{a=0}^{N-1}t^ae_a\) into a finite q-exponential column.
This is different from the ordinary binomial column in C.
For either literal signed crossing, the resulting
kernel has a nonzero analytic leading amplitude on a fixed small
donor disk. Physical recipients may lie on any buffered compact set
off incidence; factorial recipients are allowed near their lower row.
The whole meridian family, both caps, Cartan factors, and flips remain.

The new estimate uses an inverse q-difference equation in donor degree.
Its low coefficients have a uniform \(1/n\) inverse, not the artificial
binomial-slot time evolution of C and H. We prove this inversion and
its first transport below. C supplies the literal signed recurrence;
H supplies the positive spatial padding construction, which we adapt
explicitly. These are the two complete proof directs.

## 1. The literal column and its capped equation

Put
\[
 d=N-1,\quad h=N^{-1},\quad c=2\pi i,\quad
 Q=e^{ch},\quad q=e^{ch/2},\quad x=-M e^{-ch/2},\quad
 f_a=(Q;Q)_a,\quad G_Fe_a=f_ae_a.                       \tag{1}
\]
Here \(N\ge2\), and \(Q\) is fixed when \(M\ne0\) varies. In the
physical basis
\[
 Ee_a=(MQ^{-a}-M^{-1})e_{a-1}\ (a>0),\quad Ee_0=0,
 \quad Fe_a=(1-Q^{a+1})e_{a+1},\quad Fe_d=0,
 \quad Ke_a=xQ^{-a}e_a.                                \tag{2}
\]
Let \(P\) exchange the two heads and define
\[
 D e_{a,b}=x^{-a-b}Q^{ab}e_{a,b},\qquad
 \Theta=\sum_{n=0}^d\frac{(-1)^nq^{n^2}}{f_n}E_1^nF_2^n,
 \qquad
 \Theta^{-1}=\sum_{n=0}^d\frac{q^n}{f_n}E_1^nF_2^n.
                                                               \tag{3}
\]
Write \(A_+=D\Theta,\ A_-=\Theta^{-1}D^{-1}\).
The checked physical matrices are
\(R^+=\kappa P A_+\), \(R^-=\kappa^{-1}A_-P\), with their
original meridian scalar. Choose \(\epsilon=0\) for a physical
recipient and \(\epsilon=1\) for a factorial recipient, and set
\[
 G=G_{F,1}G_{F,2}^{\epsilon},\qquad
 \widetilde A_\pm=G^{-1}A_\pm G.
\]
Let \(P_a^\pm(z_1,z_2,w)\) denote the evaluation of
\(\widetilde A_\pm\) on donor \(e_a\) and recipient input
\(\sum_{b=0}^d\binom db w^b e_b\). Our actual kernel is
\[
 \mathcal C_N^\pm(z_1,z_2;t,w)
       =\sum_{a=0}^d\frac{t^a}{f_a}P_a^\pm(z_1,z_2,w).
                                                               \tag{4}
\]
Indeed \(G_F\sum t^ae_a/f_a=\sum t^ae_a\): the physical donor
input is exactly a finite geometric series, without a binomial weight.

For \(\epsilon=1\) first remove only the recipient output cap.
Its output raising operator is then multiplication by \(z_2\).
For \(\epsilon=0\) retain the actual top zero throughout:
\[
 \mathcal F=z_2(1-QT_{z_2})\quad(\epsilon=0),\qquad
 \mathcal F=z_2\quad(\epsilon=1),\qquad
 T_v:v\longmapsto Qv.                                  \tag{5}
\]
We use \(C_N^\pm\) for this auxiliary kernel; it already equals
\(\mathcal C_N^\pm\) when \(\epsilon=0\). A factorial recipient
will be projected back in Section 4. Every transfer raises it,
and its auxiliary output degree is at most \(2d\).

Set \(\lambda_+=x^{-1}\), \(\lambda_-=x\),
\(I_{\pm,h}=1+\lambda_\pm z_2w\). Then \(P_0^\pm=I_{\pm,h}^d\).
C's donor recurrences give the following operators on the entire
kernel, with all unspecified arguments unchanged:
\[
 \begin{split}
 \mathcal R_+&=x^{-1}z_1T_{z_2}
                 +\mathcal F(1-x^{-2}T_tT_{z_1}),\\
 \mathcal R_-&=xz_1T_w^{-1}
                 +\mathcal F(T_{z_1}T_w^{-1}
                                      -x^2T_t^{-1}T_w^{-1}).
 \end{split}                                                   \tag{6}
\]
The exact capped equation, for both recipient choices, is
\[
 \boxed{(1-T_t)C_N^\pm
    =t\mathcal R_\pm C_N^\pm
       -\frac{(\lambda_\pm t z_1)^N}{f_d}I_{\pm,h}^d.}   \tag{7}
\]
In fact \((1-Q^a)/f_a=1/f_{a-1}\) makes its left side
\(t\sum_{a=0}^{d-1}t^aP_{a+1}^\pm/f_a\).
The recurrence in (6) produces the same terms and one additional
top term. To compute it, append a donor symbol \(e_N\) with unit
raising from \(e_d\). Its conjugated lowering coefficient is
\((1-Q^N)(MQ^{-N}-M^{-1})=0\). Thus every positive transfer
from that symbol vanishes, for either Euler polynomial in (3).
The remaining Cartan entry is
\(x^{\mp N}x^{\mp b}Q^{\pm Nb}=x^{\mp N}x^{\mp b}\).
The same finite donor recurrence at \(a=d\) therefore produces
\(P_N^\pm=\lambda_\pm^N z_1^NI_{\pm,h}^d\), proving (7).
This device computes the omitted term; it does not enlarge the
physical module. No \(f_N\) is divided by. It also checks the
coincident root endpoint for every even or composite level.

## 2. Low-degree logarithms and the complete donor cap

Fix a buffered compact set of \(M,z_1,z_2,w\) with
\[
 M\ne0,\qquad I_{\pm,0}\ne0.                             \tag{8}
\]
For a factorial recipient also require
\(|\lambda_{\pm,0}z_2w|\le\rho<1/8\).
One sign is considered at a time, or both on the intersection.
Normalize \(B_N=C_N^\pm/I_{\pm,h}^d\). Expanding (5),(6) yields
\[
 B_N(Qt)=B_N-t\sum_\nu a_{\nu,h}e^{hY_\nu}B_N
                         +\frac{(\lambda_\pm tz_1)^N}{f_d}.
                                                               \tag{9}
\]
This specifies all coefficients without an asymptotic substitution:
divide each shifted background in (6) by \(I_{\pm,h}^d\).
Each \(Y_\nu\) is a constant integral linear combination of
\(ct\partial_t,cz_1\partial_{z_1},cz_2\partial_{z_2},cw\partial_w\).
For example the first positive coefficient and shift are
\[
 a_h=x^{-1}z_1
   \left(\frac{1+Qx^{-1}z_2w}{1+x^{-1}z_2w}\right)^d,
 \qquad Y=cz_2\partial_{z_2}.                            \tag{10}
\]
The first negative term has \(xz_1\), \(Q^{-1}\), and
\(Y=-cw\partial_w\). The remaining coefficients follow by
expanding \(\mathcal F\) in (6), including its factor \(Q\).
Background-ratio logarithms have their branch zero at \(h=0\);
with \(d=h^{-1}-1\), every \(a_{\nu,h}\) is analytic in \(h\)
on the buffers in (8). This analytic germ is an estimating device,
not an off-root finite representation.

Let \(\mathscr D=t\partial_t\) and form the logarithm
\(V_N=h\log B_N\) as a formal series with zero constant term.
For every activity degree strictly below \(N\), (9) is exactly
\[
 L_hV_N=\mathscr F_h(V_N),\qquad
 L_h=\frac{e^{hc\mathscr D}-1}{h},\qquad
 \mathscr F_h(V)=
 \log\left(1-t\sum_\nu a_{\nu,h}
             \exp\left(\frac{e^{hY_\nu}-1}{h}V\right)\right).
                                                               \tag{11}
\]
The top forcing in (9) has not been declared zero: it first
enters at degree \(N\). At degree \(n<N\) the left multiplier is
\((Q^n-1)/h\), while the right side uses only degrees below \(n\).
For any fixed \(0<\delta<1/2\),
\[
 \left|\frac{h}{Q^n-1}\right|
   =\frac{1}{2N\sin(\pi n/N)}
   \le\frac{C_\delta}{n},
 \qquad 1\le n\le\lfloor\delta N\rfloor.                \tag{12}
\]

Here is the analytic coefficient argument for this inverse, including
spatial shifts. Collapse absolute spatial Taylor coefficients to
a positive variable \(y\), and majorize the finitely many vector
fields by \(C\mathscr D+\mathcal L\), where
\(\mathcal L=C(1+y)^2\partial_y\). Let \(\phi_s\) be its positive
spatial flow. H's coefficientwise divided-difference inequality
\[
 (e^{h\mathcal L}-1)U/h
                     \preceq e^{h\mathcal L}\mathcal LU       \tag{13}
\]
and its version including \(C\mathscr D\) apply to either sign of
a clock shift after taking absolute Taylor coefficients. A shifted
input coefficient of degree \(k\) contributes only at output degree
at least \(k+1\), because (11) retains its explicit \(t\).
If that coefficient is bounded at \(\phi_{kh}(y)\), the extra
shift is bounded at \(\phi_{(k+1)h}(y)\). In products, every such
argument moves positively to the common \(\phi_{nh}(y)\) at
output degree \(n\). The factors \(e^{Ckh}\) are bounded for
\(k\le\delta N\) and are absorbed into \(C\).

Together with (12), this is a coefficient induction dominated by
\[
 \mathscr D U=
       \frac{C(y)t}{1-C(y)(t+\mathscr D U+\mathcal LU)},
 \qquad U(0,y)=0,\qquad C(y)=C/(1-y/R).                  \tag{14}
\]
For completeness, this positive majorant is analytic. Divide by
\(t\) and solve
\[
 U_t=\frac{C(y)}{1-C(y)(t+tU_t+\mathcal LU)}.             \tag{15}
\]
The implicit derivative with respect to \(U_t\) is one at \(t=0\);
its small branch is the convergent quadratic, or Catalan, series.
It is analytic with nonnegative coefficients in \(t,y,\mathcal LU\).
The resulting first-order equation \(U_t=H(t,y,U_y)\), with
initial value zero, has an analytic solution on small fixed
polydisks: its analytic characteristic ODE has an invertible
initial-to-final coordinate map for small \(t\). Positive formal
coefficient recursion agrees with that solution. This is evolution
in \(t\), not an artificial slot time.

Choose \(\delta\) smaller if needed so that \(\phi_{\delta}\) stays
in the spatial buffer. The preceding induction and Cauchy estimates give
\[
 |[t^n]V_N|\le C_1R_1^{-n},
        \qquad 1\le n\le L=\lfloor\delta N\rfloor.       \tag{16}
\]
Fixed spatial and meridian derivatives satisfy the same bound on
smaller buffers. Repeated background ratios are precisely the
ratios in (9); no unrestricted unit-time clock orbit is required.

We also need the whole finite polynomial. The recurrence for \(P_a\)
in C, or (6) coefficient by coefficient, bounds its weighted
coefficient norm by \(C^{d+a}\) on any fixed coordinate polydisk.
Physical raising coefficients have modulus at most two, and
factorial raising coefficients one; the finitely many Cartan
factors are uniformly bounded at each step on the fixed \(M\)-compact.
Moreover
\[
 |f_a|\,|f_{d-a}|=N,\qquad
 |f_a|^{-1}\le 2^{d-a}/N\le 2^d,\qquad 0\le a\le d.    \tag{17}
\]
Thus the entire sum (4), divided by its nonzero background, obeys
\(|B_N|\le e^{C_2N}\) on a fixed donor disk.

Let \(V_N^{[L]}\) be its logarithm through degree \(L\).
The functions \(B_N\) and \(e^{V_N^{[L]}/h}\) agree through that
degree. On a circle \(|t|=R_2<R_1\) both have an \(e^{CN}\)
bound. On \(|t|\le\eta R_2\), their difference is therefore at most
\(C\eta^{L+1}e^{CN}/(1-\eta)\). The comparison exponential has
modulus at least \(e^{-CN\eta R_2}\). Choosing \(\eta>0\) after
these constants gives
\[
 B_N=e^{V_N^{[L]}/h}(1+O(e^{-\gamma N})).                \tag{18}
\]
Every donor degree, including the exact forcing in (7), is now
recovered. In particular this proves actual zero-freeness on a
small fixed disk, not merely a formal logarithm.

## 3. The phase and its first transport

Write \(a_{\nu,h}=a_{\nu,0}+ha_{\nu,1}+O(h^2)\), with the literal
prescription (9). Define
\[
 Z(V)=1-t\sum_\nu a_{\nu,0}e^{Y_\nu V},\qquad
 \mathscr F_0(V)=\log Z(V),
\]
\[
 \mathscr F_1(V)=-\frac{t}{Z(V)}
       \sum_\nu e^{Y_\nu V}
       \left(a_{\nu,1}+\tfrac12a_{\nu,0}Y_\nu^2V\right).
                                                               \tag{19}
\]
The unique small analytic phase and first correction are determined by
\[
 c\mathscr D V=\mathscr F_0(V),\quad V(0)=0,
\]
\[
 (c\mathscr D-d\mathscr F_0[V])\mathcal T
       =\mathscr F_1(V)-\tfrac12c^2\mathscr D^2V,
       \qquad \mathcal T(0)=0.                         \tag{20}
\]
To obtain the first equation, divide by \(t\). Every occurrence of
\(V_t\) on its right side is multiplied by \(t\), so its implicit
derivative at \(t=0\) is \(c\ne0\). Analytic characteristics apply
as in (15). The second equation is a linear analytic transport
after the same division; its coefficient of \(\mathcal T_t\) is
\(c+O(t)\). Its forcing is analytic because all terms before division
vanish at \(t=0\). Both solutions are fixed by their zero initial data.

We record the stability argument, not just a formal expansion.
For \(W=V+h\mathcal T\), Taylor expansion of the divided shifts
in (11) gives
\[
 L_hW-\mathscr F_h(W)=O(h^2t)                           \tag{21}
\]
on smaller analytic buffers. Cauchy bounds give corresponding
coefficient estimates \(h^2 C R^{-n}\). The difference of two
right sides in (11) has a positive majorant
\(tB(t,y)(\mathscr D+\mathcal L)\) applied to their difference,
where \(B\) is analytic and bounded by the majorant already obtained
in (14). Using (12) and the same degree padding, the error is
dominated coefficientwise by \(h^2E\), where, after increasing
positive analytic coefficients, \(E\) solves
\[
 \mathscr D E=tB_0(t,y)+tB_1(t,y)\mathscr D E
                           +tB_2(t,y)\mathcal LE,\quad E(0)=0.
                                                               \tag{22}
\]
After division by \(t\), its leading derivative coefficient is
\(1-tB_1\); analytic characteristics give \(E\) on fixed small
disks. Hence
\[
 |[t^n](V_N-V-h\mathcal T)|\le h^2 C R^{-n},
                  \qquad n\le L.                     \tag{23}
\]
Summing these estimates, then using the analytic tails of \(V,\mathcal T\)
and the complete finite tail (18), proves
\[
 C_N^\pm=I_{\pm,h}^d e^{NV_\pm}
                    e^{\mathcal T_\pm}(1+O(N^{-1})).    \tag{24}
\]
There is no artificial-time endpoint correction here.
At \(t=0\), \(V_\pm=\mathcal T_\pm=0\); the amplitude is exactly
normalized to one there and is a holomorphic unit nearby.

## 4. Recipient caps, true meridian jets, and the lower chart

For a factorial recipient introduce the marker \(z_2\mapsto\xi z_2\).
Choose \(R_*>1\) with \(R_*\rho<1\) and
\[
 g=\log R_*-\log\frac{1+R_*\rho}{1-\rho}>0;
                                                               \tag{25}
\]
\(R_*=2,\rho<1/8\) suffices after a small buffer adjustment.
The preceding proof applies on this marker circle. The phase is
\(O(t)\), the amplitude a bounded unit, and the background ratio
is at most \(((1+R_*\rho)/(1-\rho))^d\).
Cauchy extraction of recipient degrees at least \(N\) supplies
\(R_*^{-N}(1-R_*^{-1})^{-1}\). Thus the projected tail is
\(O(e^{-gN+CN|t|})\) relative to (24).
Shrink the donor disk after (25). Monotone recipient raising makes
this final projection exactly the physical cap, so the theorem is
\[
 \boxed{\mathcal C_N^\pm
    =I_{\pm,h}^d e^{NV_\pm}e^{\mathcal T_\pm}
                                  (1+O(N^{-1})).}       \tag{26}
\]
For a physical recipient no output cap was removed.
The normalized remainder is holomorphic and uniformly \(O(N^{-1})\)
on fixed buffered coherent and \(M\)-domains. All fixed mixed
coherent and true fixed-\(Q\) derivatives \(\partial_\mu^k\),
\(M=e^\mu\), of this remainder have the same bound on smaller
buffers. No relative estimate is asserted for a derivative whose
own leading term vanishes.

On a selected local logarithm, the full phase is
\(\mathfrak F_\pm=\log I_{\pm,0}+V_\pm\).
Its amplitude with \(e^{N\mathfrak F_\pm}\) is the unit
\[
 \exp(\partial_h\log I_{\pm,h}|_0+\mathcal T_\pm)/I_{\pm,0}.
                                                               \tag{27}
\]
This retains the Cartan half-step and the recipient degree \(N-1\).
At completeness \(M=1,t=0\), let
\(u=\lambda_{\pm,0}z_2w/I_{\pm,0}\), \(x_{\rm cl}=-1\).
The two \(\mathcal F\) terms in (6) cancel at principal order.
Equations (19),(20) therefore give
\[
 \mathfrak F_{+,t}(0)=-c^{-1}x_{\rm cl}^{-1}z_1e^{cu},
 \qquad
 \mathfrak F_{-,t}(0)=-c^{-1}x_{\rm cl}z_1e^{-cu}.        \tag{28}
\]
The mixed matrix for output \((z_1,z_2)\), input \((t,w)\) is
triangular at that row, with nonzero diagonal entries
\[
 -c^{-1}\lambda_{\pm,0}e^{\pm cu},\qquad
                         \lambda_{\pm,0}/I_{\pm,0}^2.  \tag{29}
\]
It remains nondegenerate nearby.

The input dictionary is also literal. In the factorial donor frame,
put \(\widetilde F=G_F^{-1}FG_F\). For
\(\psi(t)=\sum_{a=0}^d t^ae_a/f_a\),
\[
             t\widetilde F\psi(t)=(1-T_t)\psi(t).       \tag{30}
\]
Thus with occupation \(u_1=t\mathfrak F_t\) and
\(A_1=e^{cu_1}\), the complete physical chart has
\[
        p_1=t,\qquad f_1=\frac{1-A_1}{t},\qquad f'_1=z_1.
                                                               \tag{31}
\]
The removable value at \(t=0\) is
\(-c\mathfrak F_t=\lambda_{\pm,0}z_1e^{\pm cu}\).
For \(z_1\ne0\) this is a resolved lower \(f\)-unit point.
There is no ordinary-binomial factor \(1-u_1\) in (31).
The output donor raising row is multiplication by \(z_1\) apart
from its top endpoint. Since donor output degree never exceeds
donor input degree, that endpoint has activity at least \(d\).
The same complete-polynomial bound and smaller-disk tail argument
as (18) make it exponentially small relative to (26). Thus the
displayed output symbol also retains its actual finite cap.
The exact \(F\) and Cartan relations suffice for this identification;
no uncapped \(E\)-column relation is used.

Finally the checked crossing has the exact frame interfaces
\[
 (PGP)^{-1}R^+G=\kappa P\widetilde A_+,\qquad
 G^{-1}R^-(PGP)=\kappa^{-1}\widetilde A_-P.               \tag{32}
\]
The positive kernel exchanges output variables; the negative one
exchanges input variables. Original pivots and inverse incident
frames stay on the network. Standard zero framing leaves the
additional factor \(x^{\pm d}\), with every true meridian derivative.

This is a local theorem for this geometric series as input. It does not
estimate a full quotient section \(S_m\psi(t)\), its returning
\(q_F\) row, or the original closing relative cycle. In a later
section formula with two finite endpoint terms, both remain,
including at a coalescence such as \(ay=1\). The present result
does not put an arbitrary \(aF_{\rm r}\), nonlower geometric donor,
or whole braid word into its small disk. It supplies the actual
local factor and its normal family without replacing those adapters.

## Complete proof-source pins

* C: notes/research_physical_crossing_hybrid_lower_kernel.md,
  398 lines, SHA256
  3025b561b9e30503de6eb2fe6ca265f04cfa730313c77c2156d3fc3b35f8926f.
* H: notes/research_hybrid_spin_euler_star_lower_chart.md,
  696 lines, SHA256
  1575d7cee6c12c7d9c6ada57a7be61eecccf4b637cdc70ed7777fc7b9b620b93.

Both complete directs were freshly read nontruncated in this active
author sequence. The entire matching final was read back, every used
implication checked, and all three hashes renewed before freezing.
Only written mathematics and text/hash operations were used; frozen
and public files are unchanged.
