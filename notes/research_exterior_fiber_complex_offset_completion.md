# A holomorphic cap completion of the actual exterior fiber

Private written proof, 19 November 2026.

The physical exterior fiber has a cap which changes with its integer
offsets. This note supplies one fixed finite sum on a complex offset
neighborhood. It agrees exactly with every nearby admissible integer
fiber: all added terms contain an actual factorial zero. The completed
sum has the same nonzero Gaussian coefficient, uniformly on that
complex neighborhood. Its proof retains the entire completed interval,
including points beyond the physical cap.

This is a specified holomorphic interpolation, not an off-grid physical
operator or a meridian family. The original integer values and the
finite contour coefficient are fixed; no uniqueness of off-grid
interpolation is asserted. The untouched exterior source is retained.

The complete directs are Z, the actual fiber closing theorem, F, the
exact sine-factorial interpolation, and E, the full finite source used
only to specify the outside normalization.

## 1. Data, fixed completion, and the assertion

Write \(c_0=2\pi i\), \(Q=e^{c_0/N}\), \(d=N-1\), and
\[
 G_N(n)=S_n=\prod_{j=1}^n2\sin(\pi j/N),\qquad 0\le n<N.
 \tag{1}
\]
Here \(G_N\) is F's exact Gamma-product function, with its fixed
positive-real marks. Fix \(k\ge2\) and any real criterion base of Z:
\[
 A_i^*>0,\quad B_i^*\ge0,\quad \min_iB_i^*=0,\quad
 A_i^*+B_i^*<1,\quad \cot^2(\pi A_i^*)<8 .
 \tag{2}
\]
Put \(\kappa_*=1-\max_i(A_i^*+B_i^*)>0\), and let
\[
 R_*(y)=\sum_i[J(A_i^*+B_i^*+y)-2J(B_i^*+y)],
 \quad J(x)=\int_0^x\log(2\sin\pi v)\,dv .
 \tag{3}
\]
Its unique maximum \(y_0\in(0,\kappa_*)\) is supplied by Z's
written full-interval concavity proof. Assume Z's actual resonance
condition
\[
 \pi\{k y_0+\sum_iB_i^*-\sum_iA_i^*-k/2\}=2\pi n,
                         \qquad n\in\mathbb Z .
 \tag{4}
\]
Z supplies such bases for every fixed \(k\ge2\).

Choose a sufficiently small fixed \(\delta_1>0\), as specified below,
and use the single cutoff
\[
                L_N=\lfloor N(\kappa_*+\delta_1)\rfloor .
 \tag{5}
\]
It depends on the chosen base and N, not on the varying offsets.
For complex \(A,B,t\) near \(A^*,B^*,1\), define the finite sum
\[
 \begin{split}
 {\cal H}_{N,+}(A,B,t)
   =\sum_{l=0}^{L_N}
    &\prod_{i=1}^k
       \frac{G_N(N(A_i+B_i)+l)}{G_N(NB_i+l)^2}\\
    &{}\times
      e^{\,iN\phi(A,B,l/N)}
      e^{\,i\pi(k/2-2)l/N}t^l,\\
 \phi(A,B,y)&=\pi\{ky^2/2+
                   y(\sum_iB_i-\sum_iA_i-k/2)\}.
 \end{split}                                                   \tag{6}
\]
Every quotient in (6) means the product of G and the square of
its holomorphic reciprocal on their respective half-planes.
Define the negative sign by Schwarz reflection of this entire
formula,
\[
 {\cal H}_{N,-}(A,B,t)
       =\overline{{\cal H}_{N,+}(\bar A,\bar B,\bar t)} .
 \tag{7}
\]
This is holomorphic in \(A,B,t\); it is not a Hermitian dual
applied to a moving source vector.

**Completion theorem.** There are \(\delta_1>0\), a fixed complex
polydisk \({\cal U}\) about \((A^*,B^*)\), a fixed disk
\(|t-1|<r\), and \(N_0\), on which (6) is holomorphic and
nonzero for every \(N\ge N_0\). For every literal admissible fiber
\[
 A_i=a_i/N,\quad B_i=b_i/N,\quad a_i,b_i\ge0,\quad
 \min_i b_i=0,\quad K=d-\max_i(a_i+b_i)\ge0
 \tag{8}
\]
in that neighborhood, its exact original polynomial obeys
\[
 F_{\gamma,\varepsilon}(t)
             ={\cal E}_{\gamma,N}^{\varepsilon}
                       {\cal H}_{N,\varepsilon}(A,B,t).
 \tag{9}
\]
The factor \({\cal E}_{\gamma,N}^{\varepsilon}\) is Z's literal
factor, including its original initial coefficient. In particular
(9) is exact, not an asymptotic comparison at integer offsets.

The nonzero asymptotic of (6) is explicit. On the protected central
logarithmic branches put
\[
 \begin{split}
 \Psi(A,B,y,t)
   &=\sum_i[J(A_i+B_i+y)-2J(B_i+y)]
       +i\phi(A,B,y)-2\pi i n y+y\operatorname{Log}t,\\
 {\cal A}(A,B,y)
   &=e^{i\pi(k/2-2)y}
       \prod_i\frac{\sqrt{2\sin\pi(A_i+B_i+y)}}
                        {2\sin\pi(B_i+y)} .
 \end{split}                                                   \tag{10}
\]
Here \(\operatorname{Log}1=0\), and all square roots continue
their positive-real marks at the base. The critical point
\(y_*(A,B,t)\) near \(y_0\) is holomorphic. With
\(H=-\Psi_{yy}(A,B,y_*,t)\), and its square root continued
through \(\operatorname{Re}H>0\),
\[
 \boxed{\displaystyle
 {\cal H}_{N,+}
   =N^{(1-k)/2}e^{N\Psi(A,B,y_*,t)}
       \frac{\sqrt{2\pi}\,{\cal A}(A,B,y_*)}{\sqrt H}
                         (1+O(N^{-1})).}
 \tag{11}
\]
The relative error is holomorphic and uniformly \(O(N^{-1})\)
on a slightly larger parameter neighborhood than any final
closed polydisk under discussion. All fixed derivatives of that
relative error satisfy the same order on smaller polydisks.
Formula (7) gives the marked negative-sign assertion.

## 2. The whole half-planes and their endpoint bound

F defines
\[
 G_N(z)=(2\pi/N)^z\Gamma(1+z)
    \prod_{\nu\ge1}
       \frac{\Gamma(N\nu+z+1)}
            {\Gamma(N\nu-z)(N\nu)^{2z+1}} .
 \tag{12}
\]
The tail logarithms converge locally uniformly with order
\(O(\nu^{-2})\). The same estimate holds on every fixed compact
set away from the finitely many early Gamma factors; this follows
by their same large-\(\nu\) ratio expansion.

For \(\operatorname{Re}z>-1\), all numerator Gamma factors are
holomorphic and nonzero, while reciprocal denominator Gamma
factors are entire. Thus G is holomorphic on that half-plane.
For \(\operatorname{Re}z<N\), apply the same argument to the
reciprocal product: its numerator Gamma arguments \(N\nu-z\)
have positive real part and all reciprocal denominator factors
are entire. Thus \(1/G_N\) is holomorphic on this second
half-plane. Negative integer zeros of the reciprocal and positive
integer zeros of G are allowed in these statements.

In particular the exact functional equation of F gives
\[
 G_N(z+1)=2\sin(\pi(z+1)/N)G_N(z),\qquad
               G_N(j)=0\quad(N\le j<2N).
 \tag{13}
\]
The zeros in the displayed interval also follow directly from
the \(\nu=1\) reciprocal Gamma factor in (12).
Reflection extends as a meromorphic identity:
\[
                   G_N(z)G_N(N-1-z)=N .
 \tag{14}
\]

We need an upper bound which tolerates these zeros. There are
absolute \(C,\delta_0>0\) such that, for each fixed
\(0<\delta<\delta_0\), and sufficiently large N,
\[
 \begin{split}
 \sup_{|w|\le\delta}|1/G_N(Nw)|
      &\le C_\delta N^C
                    e^{CN\delta(1+|\log\delta|)},\\
 \sup_{|w-1|\le\delta}|G_N(Nw)|
      &\le C_\delta N^C
                    e^{CN\delta(1+|\log\delta|)} .
 \end{split}                                                   \tag{15}
\]
Constants may be enlarged between the lines.

Here is an elementary proof, including negative real parts in
the first disk. Put \(j=\lceil2\delta N\rceil\) and take
\(N\ge1/\delta\). Iterating (13) for the reciprocal gives
\[
 \frac1{G_N(Nw)}
    =\frac{\prod_{h=1}^j2\sin\pi(w+h/N)}
                  {G_N(Nw+j)} .
 \tag{16}
\]
This is a holomorphic identity, including at zeros on the left.
Each numerator factor has modulus at most \(C\delta\le1\)
after a fixed choice of \(\delta_0\). The shifted scaled
argument has real part between \(\delta\) and \(4\delta\)
and imaginary part at most \(\delta\). It therefore belongs
to a protected compact subset of F's strip. On that set
\[
 |J(z)|\le C\delta(1+|\log\delta|).
 \tag{17}
\]
Indeed \(\log(2\sin\pi z)=\log z+\log(2\pi)+O(z^2)\)
with its continued mark, and the primitive of \(\log z\)
is \(z\log z-z\); the remaining analytic primitive is
\(O(|z|^3)\). F's uniform formula for \(G_N(Nz)\), applied
to the denominator of (16), proves the first bound (15).
Its fixed-\(\delta\) square-root and remainder factors cost
at most \(C_\delta N^C\). Finally (14) gives
\[
 G_N(Nw)=N/G_N(N(1-w)-1).
 \tag{18}
\]
For \(|w-1|\le\delta\), the new scaled argument has modulus
at most \(2\delta\) for large N. The first bound proves the
second. No lower bound for G at one of its zeros is used.

## 3. Exact finite completion and the retained outside scalar

Let \(\alpha_*=\min_iA_i^*>0\).
First take \(\delta_1<\alpha_*/8\) and then take the parameter
radius \(\epsilon\) small compared with \(\delta_1\), for example
\(2\epsilon<\delta_1/2\). On the whole sum \(0\le l\le L_N\),
\[
 \operatorname{Re}(A_i+B_i+l/N)>0,\qquad
 \operatorname{Re}(B_i+l/N)<1-\alpha_*/2
 \tag{19}
\]
after a further fixed shrink. The first assertion also uses
\(A_i^*+B_i^*\ge\alpha_*\); the second follows from
\(B_i^*+\kappa_*\le1-A_i^*\).
Thus the half-plane results prove joint holomorphy of every
term of (6), even when a complex B has negative real part.

At literal integer data (8), sufficiently large N satisfies
\[
 K<L_N<d-\max_i b_i .
 \tag{20}
\]
The first inequality follows from
\(|\max_i(A_i+B_i)-\max_i(A_i^*+B_i^*)|\le2\epsilon\);
the second follows from (19) with its fixed margin.
For any \(l>K\) choose an index attaining \(\max_i(a_i+b_i)\).
Its numerator index is at least N. All numerator indices in
the completed interval are less than 2N, since
\(\max_i(A_i+B_i)+L_N/N<1+\delta_1+2\epsilon<2\).
Equation (13) makes the added term zero. All denominator
indices are between zero and d by (20). Hence no zero is
divided by another zero. For \(l\le K\), every G value is
the original sine factorial. Z's exact formula (7) proves (9).

The normalization in (9) has no hidden \(b_i\)-pole. To see
its original meaning, separate E's initial source coefficient
into its untouched exterior factor and the k displayed rows:
\[
 T_{\gamma,0}^{\varepsilon}
    =\Theta_{\gamma,N}^{\varepsilon}
       \prod_i(S_{a_i}^2S_{b_i}^2S_{d-a_i-b_i})^{-1}.
 \tag{21}
\]
The factor \(\Theta_{\gamma,N}^{\varepsilon}\) retains the
complete initial phase, original pivot and all unaffected
source factors. Z defines
\({\cal E}=T_{\gamma,0}\prod_i S_{b_i}^2/S_{a_i+b_i}\).
Exact reflection \(S_jS_{d-j}=N\) therefore yields
\[
 {\cal E}_{\gamma,N}^{\varepsilon}
      =\Theta_{\gamma,N}^{\varepsilon}
                         N^{-k}\prod_iS_{a_i}^{-2}.
 \tag{22}
\]
The explicit right-hand factorials have a holomorphic unit
continuation by \(G_N(NA_i)^{-2}\) near the present base.
No estimate or holomorphic continuation of the untouched
factor \(\Theta_{\gamma,N}^{\varepsilon}\) is inferred here.

## 4. A uniform gap on the whole completed interval

This step is an actual complex-parameter bound; it is not an
analytic continuation of an estimate known only at integer offsets.
Let \(M_*=R_*(y_0)\). By Z's strict full-interval concavity,
both \(R_*(0)\) and \(R_*(\kappa_*)\) are strictly below \(M_*\).
Fix a small protected central interval about \(y_0\).
Its complement in \([0,\kappa_*]\) has a fixed positive gap.

Choose \(\delta>0\) small compared with that interval and with
all positive distances of the base factorial arguments from 0
and 1 at the two endpoints. Only exact endpoint arguments need
the bounds (15). At \(y=0\) these are precisely denominators
with \(B_i^*=0\). At \(y=\kappa_*\) these are precisely
numerators with \(A_i^*+B_i^*+\kappa_*=1\).
All other endpoint arguments have fixed protected neighborhoods.
Shrinking delta further makes
\(C\delta(1+|\log\delta|)\) smaller than a prescribed fraction
of the endpoint and central-complement gaps.

Now choose \(0<\delta_1<\delta/4\) in (5), also satisfying
Section 3, and finally shrink the complex parameter and t disks.
For \(0\le y\le\delta\), (15) for the active denominator
reciprocals and F's protected expansion for the other factors
give the following bound for the summand of (6):
\[
 |\text{summand at }y|
   \le N^{C_1}
       \exp N\{R_*(0)+C_2\delta(1+|\log\delta|)
                           +C_3\epsilon+C_3|\operatorname{Log}t|\}.
 \tag{23}
\]
The harmless constant can depend on the fixed base and delta.
This comparison retains the entire phase in (6): at real base
data it has modulus one; its change on the complex parameter
disk costs at most \(e^{NC_3\epsilon}\). Its subprincipal
factor is bounded uniformly.

For \(\kappa_*-\delta\le y\le L_N/N\), use instead the
second bound (15) at every active numerator and the protected
expansion at the denominators and remaining numerators. This gives
the same expression with \(R_*(\kappa_*)\) replacing \(R_*(0)\).
This is also a bound beyond the physical cap. It neither continues
the positive sine logarithm across a zero nor assumes the continued
envelope decreases there.

On the remaining real interval all arguments lie in a protected
strip. F gives the bound \(N^{C_1}e^{NR_*(y)+O(N\epsilon)
+O(N|\operatorname{Log}t|)}\) uniformly. Outside the central
interval its real-base gap persists. With the stated ordered
choices, summing at most \(L_N+1=O(N)\) terms yields
\[
 \left|\sum_{\text{outside central}} \text{summand}\right|
                         \le N^{C_4}e^{N(M_*-g)},\qquad g>0,
 \tag{24}
\]
uniformly throughout a fixed complex parameter polydisk.
In fact the sum of the absolute values has this bound.

## 5. The same original finite contour selects the coefficient

Inside the central interval all factorial arguments have
protected real parts. For complex A,B near the base, the exact
interpolated summand, with the lattice-one factor
\(e^{-2\pi i nNy}\), is therefore
\[
 f_N(y;A,B,t)=N^{-k/2}e^{N\Psi(A,B,y,t)}
                    ({\cal A}(A,B,y)+O(N^{-1})).
 \tag{25}
\]
It is holomorphic jointly in y,A,B,t on a fixed larger
rectangle and parameter neighborhood. At \(y=l/N\) it is
exactly the completed summand, for every complex offset,
because the inserted alias factor is one.

At the real base and \(t=1\), (4) makes \(\Psi_y(y_0)=0\)
and Z proves \(\operatorname{Re}(-\Psi_{yy}(y_0))>0\).
The analytic implicit function theorem gives \(y_*\) and H
on a fixed complex parameter disk. Choose the central half-width
first, so the unshifted real-axis endpoints have a strict gap
and \(|\phi_y-2\pi n|<\pi/4\) there. Choose the rectangle
height smaller than that gap and the square of its width.
Then shrink all complex parameter disks. Exactly as in Z's
finite rectangle proof, its vertical sides remain below the
critical real action, and the upper/lower bounds satisfy
\[
 \sup_{\text{horizontal sides}}\operatorname{Re}\Psi
                    -\operatorname{Re}\Psi(y_*)<\pi h .
 \tag{26}
\]
These are uniform open inequalities, hence the same choices
work for the complex offsets; no real-offset positivity is
being invoked after the shrink.

Put the vertical sides at the enclosing half-grid coordinates.
The exact cotangent residue identity gives the central finite
sum. Its top and bottom expansions are
\(\cot(\pi N(x+ih))=-i+O(e^{-2\pi Nh})\) and
\(\cot(\pi N(x-ih))=i+O(e^{-2\pi Nh})\).
By (26) both remainder terms are exponentially below the saddle.
The vertical sides have their strict gap. With the original
counterclockwise orientation, the two constant terms each give
one half of N times a horizontal integral. Translate both
segments to the line through \(y_*\), keeping the gapped side
connectors. Their sum is thus N times one oriented integral,
with coefficient exactly \(+1\).

On that line the real quadratic part is uniformly negative.
The ordinary complex Gaussian estimate applied to (25) gives
(11), with relative \(O(N^{-1})\); the square root is the
continuous one through \(\operatorname{Re}H>0\).
This is the same local estimate as Z, now on a joint analytic
rectangle. Its nonzero coefficient is bounded away from zero.
The critical real action stays within \(g/4\) of \(M_*\)
after shrinking parameters, so (24) is exponentially relative.
All removed completed terms, cap layers, connectors and local
alias remainders are therefore paid on that common neighborhood.

Because the finite sum and normalized leading expression are
jointly holomorphic on a larger neighborhood, Cauchy's formula
gives the stated bounds for all fixed derivatives of the relative
error on smaller polydisks. In particular (11) proves actual
zero-freeness of the completed sum for sufficiently large N.

## 6. Scope of the new continuation

The exact completed equation also records its endpoint dependence.
Write \({\cal H}_{N,\varepsilon}=\sum_{l=0}^{L_N}h_l^\varepsilon t^l\)
and set
\[
 \alpha_i=e^{c_0(A_i+B_i)},\quad \beta_i=e^{c_0B_i},\quad
 P(v)=\prod_i(1-\beta_i v)^2,\quad
 R(v)=\prod_i(1-Q\alpha_i v),\quad
 c_+=(-1)^kQ^{k-1}e^{c_0\sum_i(B_i-A_i)}.
 \tag{27}
\]
The exact sine shift (13), including both phase factors in (6),
gives the cleared coefficient rows
\[
 \begin{split}
 P(Q^{l+1})h_{l+1}^+
       &=c_+Q^{kl}R(Q^l)h_l^+,\\
 P(Q^{l+1})h_{l+1}^-
       &=Q R(Q^l)h_l^- .
 \end{split}                                                   \tag{28}
\]
For example
\(2\sin\pi z=i e^{-\pi i z}(1-e^{c_0z})\);
substitution in the ratio of successive terms gives respectively
the constants \(c_+Q^{kl}\) and Q. Thus (28) holds holomorphically
even when either coefficient vanishes; it does not divide by that
coefficient. If \(\mathsf T f(t)=f(Qt)\), summing this row yields
\[
 \begin{split}
 [P(\mathsf T)-c_+t\mathsf T^kR(\mathsf T)]{\cal H}_{N,+}
     &=P(1)h_0^+
       -c_+Q^{kL_N}R(Q^{L_N})h_{L_N}^+t^{L_N+1},\\
 [P(\mathsf T)-QtR(\mathsf T)]{\cal H}_{N,-}
     &=P(1)h_0^-
       -Q R(Q^{L_N})h_{L_N}^-t^{L_N+1}.
 \end{split}                                                   \tag{29}
\]
At the physical data (8), \(P(1)=0\) because some \(b_i=0\),
and \(h_{L_N}^\varepsilon=0\) by (20). The original homogeneous
equation in E is recovered. Off that lattice the displayed
endpoint forcing must be retained.

The physical endpoint K varies with the integer data; the chosen
endpoint \(L_N\) does not. Equations (13) and (20) are the reason
this fixed sum still has exactly the original values at every
nearby admissible integer tuple. A different longer off-grid
completion need not agree as a holomorphic function. Only the
specified completion (6), with its controlled short added interval,
is asserted here.

Its derivatives in complex A,B belong to that specified function.
They are not meridian derivatives of the quantum module, Casimir
Hermite partners, or derivatives of an unspecified exterior
intertwiner. No condition or estimate for the remaining sum over
gamma is obtained by discarding the exact factor (22).
Likewise the theorem does not identify a geometric offset tuple,
select the full original closed-source cycle, or prove a volume
limit. It supplies a local holomorphic boundary function with
literal finite source values, an actual nonzero contour coefficient,
and all its completed tails controlled.

## Complete direct sources

* Z: notes/research_exterior_fiber_zero_free_closing.md, 514 lines,
  SHA256 8b7d5a5eae77b98fb9f531fb1a8d03ad5e5a808978e66eb854431b468ce25d92.
* F: notes/exact_factorial_interpolation_and_complex_contours.md,
  226 lines, SHA256
  1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.
* E: notes/research_exterior_pivotal_fiber_quantum_curve.md,
  422 lines, SHA256
  b214fcb13fcb0eccc42f82597d9eef5aaa77315a2e0014485754df0e3af44fac.

All additional half-plane, endpoint and completion arguments are
written above. Only written mathematics and text/hash operations
were used; frozen and public sources remain unchanged.
