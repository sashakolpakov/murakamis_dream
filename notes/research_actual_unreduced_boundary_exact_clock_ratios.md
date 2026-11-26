# Boundary-exact unreduced ratios of the original highest-cut source

Private written proof, 18 November 2026.

For the original one-component highest-cut source, its support is
exactly the nonnegativity of the two inverse-factorial lengths at
each crossing. Those inverse factorials already supply the correct
one-sided zeros when a lattice shift crosses the support boundary.
Keeping the productwise ratio unreduced therefore gives exact joint
clock equations without the additional common boundary multiplier
used in [J].

The natural factors in these equations must still be retained.
The result does not divide their possible zeros or establish an
analytic inverse for the internal clock system.

## 1. The exact support on the matching lattice

Use the fixed integral matching lattice \(k\in\mathbb Z^d\) of [J]
for the original knot braid, including the two cut occupations zero.
Every strand occupation and crossing transfer is an integral linear
form in \(k\). The closed braid permutation has one cycle.
Write \(n_c\) for the transfer at crossing \(c\), and define
\[
 o_c=
 \begin{cases}
   a_c-n_c,&c\text{ positive},\\
   b_c-n_c,&c\text{ negative},
 \end{cases}
 \tag{1}
\]
where \(a_c,b_c\) are its two input occupations. The letter \(o_c\)
is the physical over-strand output. The original crossing support
in [F] requires nonnegative occupations and
\(0\le n_c\le a_c\) or \(0\le n_c\le b_c\), respectively.

**Support lemma.** On this entire matching lattice, the original
support is exactly
\[
              \mathcal P=\{k:n_c(k)\ge0,\ o_c(k)\ge0
                                      \text{ for every }c\}.
 \tag{2}
\]

To prove the nontrivial inclusion, start at the cut occupation zero
and follow the oriented physical knot. At a positive crossing the
physical input \(a\) leaves as \(a-n=o\), and the physical input
\(b'\) leaves as \(b'+n\). At a negative crossing the physical
input \(b'\) leaves as \(b'-n=o\), and the physical input \(a\)
leaves as \(a+n\). Thus an underpass adds \(n\ge0\) to the current
occupation, and an overpass exits with \(o\ge0\). Induction along
the component makes every traversed segment nonnegative.
The one-cycle hypothesis says that every physical segment is
visited. Moreover the over-input is identically \(n+o\), so all
transfer upper bounds hold. This proves (2). The converse follows
immediately from the original support conditions.

The argument retains the highest cut. In particular a zero
over-input forces \(n=o=0\), exactly as in the original vacuum
columns. There is no extra free trace component to which this
induction has not been applied. The lemma is not asserted for
an uncut multi-component trace.

## 2. A signed finite-product convention

For an integer \(d\) and an independent nonzero variable \(t\),
define the two polynomials
\[
 U_d(t)=
 \begin{cases}
  \prod_{r=0}^{d-1}(1-tQ^r),&d>0,\\
  1,&d\le0,
 \end{cases}
 \qquad
 V_d(t)=
 \begin{cases}
  \prod_{r=d}^{-1}(1-tQ^r),&d<0,\\
  1,&d\ge0,
 \end{cases}
 \tag{3}
\]
and their rational quotient
\[
                         P_d(t)=U_d(t)/V_d(t).
 \tag{4}
\]
All products in (3) have fixed finite length. Negative powers of
\(Q\) are allowed. The elementary cocycle identity is
\[
                 P_{r+s}(t)=P_r(t)P_s(tQ^r).
 \tag{5}
\]
It follows by concatenating the two oriented integer intervals,
or canceling their oppositely oriented overlap.

Put \(F_L=(Q;Q)_L\) only for \(L\ge0\). If \(L,L+d\ge0\), then
\[
                         F_{L+d}/F_L=P_d(Q^{L+1}).
 \tag{6}
\]
No value of \(F_L\) at a negative integer will be used.
The right side of (6), after separate numerator and denominator
clearing by (3), is a Laurent-polynomial expression that can be
evaluated at every lattice point.

We will multiply the numerators and denominators furnished by
(3) separately. No common factors will be canceled between them,
either within one crossing or between different crossings.

## 3. The literal factors and their proper shifted ratios

Set \(Q=q^2\), \(Y=Qx^2\), and let
\(c=b-1-\operatorname{wr}(\beta)\in2\mathbb Z\).
The entries [F, (2)] can be written, on their support, as
\[
\begin{split}
 R^+&=x^{-a-b'+n}Q^{ob'}
       \frac{F_{n+o}}{F_nF_o}
                    (Y^{-1}Q^{o+1};Q)_n,
                  &&a=n+o,\\
 R^-&=x^{a+b'-n}Q^{-ab'}
       \frac{F_{n+o}}{F_nF_o}
                    (YQ^{-n-o};Q)_n,
                  &&b'=n+o .
\end{split}
 \tag{7}
\]
The factorial quotients are interpreted as their original Gaussian
polynomials at special parameters. For deriving their proper
ratios we first use generic \(Q,Y\).

Fix any lattice step \(v\in\mathbb Z^d\) and any external shift
\(j\in\mathbb Z\). Let
\[
        \Delta n=n(v),\qquad \Delta o=o(v)
 \tag{8}
\]
at each crossing. The new arguments are \(k+v\) and \(Y'=Q^jY\).
For the Gaussian factor in either sign, its common-support ratio is
\[
 \frac{P_{\Delta n+\Delta o}(Q^{n+o+1})}
      {P_{\Delta n}(Q^{n+1})P_{\Delta o}(Q^{o+1})}.
 \tag{9}
\]
In its unreduced polynomial numerator and denominator this becomes
\[
\begin{split}
 A_{\mathrm G}&=
 U_{\Delta n+\Delta o}(Q^{n+o+1})
 V_{\Delta n}(Q^{n+1})V_{\Delta o}(Q^{o+1}),\\
 B_{\mathrm G}&=
 V_{\Delta n+\Delta o}(Q^{n+o+1})
 U_{\Delta n}(Q^{n+1})U_{\Delta o}(Q^{o+1}).
\end{split}
 \tag{10}
\]

For clarity the color-product ratios are also completely explicit.
For \(n,n+\Delta n\ge0\), (5) gives
\[
 \frac{(tQ^d;Q)_{n+\Delta n}}{(t;Q)_n}
                =\frac{P_{d+\Delta n}(tQ^n)}{P_d(t)} .
 \tag{11}
\]
At a positive crossing this is
\[
 \frac{P_{\Delta o+\Delta n-j}(Y^{-1}Q^{n+o+1})}
      {P_{\Delta o-j}(Y^{-1}Q^{o+1})};
 \tag{12}
\]
at a negative crossing it is
\[
 \frac{P_{j-\Delta o}(YQ^{-o})}
      {P_{j-\Delta n-\Delta o}(YQ^{-n-o})}.
 \tag{13}
\]
For any quotient \(P_r(t_1)/P_s(t_2)\) in (12)--(13), define its
unreduced numerator to be \(U_r(t_1)V_s(t_2)\), and its
denominator \(V_r(t_1)U_s(t_2)\). These are Laurent polynomials
after substituting the lattice characters \(X_i=Q^{k_i}\).
They are finite products even off the support; no negative-length
color product is evaluated there.

It remains to retain the whole monomial, including the closing.
Define integral forms
\[
\begin{split}
 H(k)&=\sum_-(a+b'-n)+\sum_+(-a-b'+n),\\
 \Omega(k)&=-T(k)+\sum_+ob'-\sum_-ab'.
\end{split}
 \tag{14}
\]
The first is linear. The second has degree at most two and
\(\Omega(0)=0\). The source [J] is exactly, on its support,
\[
 \mathcal I(Q,x,\tau;k)
     =x^{c+H(k)}\tau^{T(k)}Q^{\Omega(k)}
           \prod_c\left[
             \frac{F_{n_c+o_c}}{F_{n_c}F_{o_c}}
                         \mathcal C_c(Y,Q;k)\right],
 \tag{15}
\]
where \(\mathcal C_c\) is the color product in (7).

The staggered parity in [F] shows that \(H\) is even on the
entire integral matching lattice: the local output/input signs
telescope pathwise through the original cut and closing. Thus
\(H/2\) and \(H(v)/2\) are integral. Define the integral linear form
\[
              \lambda_v(k)=\Omega(k+v)-\Omega(k)-\Omega(v).
 \tag{16}
\]
The exact monomial ratio of (15), including \(x\mapsto q^jx\), is
\[
 \mathcal M_{j,v}
  =\tau^{T(v)}Y^{H(v)/2}
      Q^{\,\Omega(v)+jc/2+(j-1)H(v)/2}
                         X^{\,\lambda_v+jH/2}.
 \tag{17}
\]
Indeed \(x^{H(v)}=(Y/Q)^{H(v)/2}\), while the external shift
contributes \(Q^{j(c+H(k)+H(v))/2}\).
The pivot is the \(-T\) term of \(\Omega\), and the framing is
the \(jc/2\) term. No square-root meridian or extra phase remains.

Define \(\mathcal A_{j,v}\) to be (17) times all crossing
numerators from (10), (12), and (13), and define
\(\mathcal B_{j,v}\) to be the product of all their denominators.
These are fixed Laurent polynomials in \(Q,Y,\tau,X\).
On every common supported pair their proper ratio is
\[
 \frac{\mathcal I(Q,q^jx,\tau;k+v)}
      {\mathcal I(Q,x,\tau;k)}
             =\frac{\mathcal A_{j,v}(Q,Y,\tau,X)}
                    {\mathcal B_{j,v}(Q,Y,\tau,X)}.
 \tag{18}
\]
Equation (18) is used only generically; its cleared version is
the assertion needed below.

## 4. The inverse-factorial zeros pay the boundary exactly

Extend \(\mathcal I\) by zero outside (2), as in [J].
Let \(S^v f(k)=f(k+v)\), and let \(\mathsf T^j\) shift
\(Y\) to \(Q^jY\). Then the following identity holds on the
entire integer lattice:
\[
 \boxed{\quad
 \bigl(\mathcal B_{j,v}\mathsf T^jS^v
                         -\mathcal A_{j,v}\bigr)\mathcal I=0 .
 \quad}
 \tag{19}
\]
The coefficients in (19) are evaluated at the old \(k,Y\),
in the displayed left ordering.

There are four cases.
If both points are supported, (19) is the cleared proper ratio
(18), first at generic parameters and then by Laurent-polynomial
continuation. If neither point is supported, both source terms
are zero.

Suppose the old point is unsupported and the new point is
supported. By the exact support lemma, some inverse-factorial
length \(L=n_c\) or \(o_c\) satisfies
\[
                       L(k)<0,\qquad L(k)+L(v)\ge0 .
 \tag{20}
\]
Write \(\Delta=L(v)>0\). Its factor in \(\mathcal B_{j,v}\)
is, from (10),
\[
 U_\Delta(Q^{L(k)+1})
              =\prod_{r=1}^{\Delta}(1-Q^{L(k)+r}).
 \tag{21}
\]
The integer \(r=-L(k)\) belongs to this range, so (21)
contains \(1-Q^0=0\). Hence
\(\mathcal B_{j,v}\mathcal I(Q,q^jx,\tau;k+v)=0\).
The other source value was zero already.

Conversely, if the old point is supported and the new point is
unsupported, some such length has
\[
                       L(k)\ge0,\qquad L(k)+\Delta<0,
                                  \qquad \Delta<0 .
 \tag{22}
\]
Its factor in \(\mathcal A_{j,v}\) is
\[
 V_\Delta(Q^{L(k)+1})
                 =\prod_{r=\Delta+1}^{0}(1-Q^{L(k)+r}).
 \tag{23}
\]
Now \(r=-L(k)\) lies in the indicated range. This factor kills
the old supported source term. The new source term is zero.
This proves (19) in every case.

All other factors in \(\mathcal A,\mathcal B\) are Laurent
polynomials after the separate clearing. They cannot turn the
zero in (21) or (23) into an indeterminate quotient, since no
factor has been canceled. Numerator factorials crossing their
own zero indices therefore cause no exception. Neither do color
zeros or special values of \(Q\): every supported entry is its
original Laurent polynomial, and (19) has already been cleared.
The torus parameters \(Q,Y,\tau\) are nonzero.

The displayed coefficient polynomials are not identically zero.
For a factorial factor \(1-Q^rX^L\) to be identically zero,
one needs \(L=0\) as a lattice form and \(r=0\). But then
\(\Delta=L(v)=0\), and that factorial ratio contributes no
factors at all. The same reasoning applies to the numerator
length \(n+o\). Every color factor additionally contains
\(Y\) or \(Y^{-1}\), so it is nonzero as a Laurent polynomial.
The monomial (17) is a unit. The trivial shift \(j=0,v=0\)
of course gives the trivial equation \(0=0\), as it should.

## 5. Exact clock equations and the surviving localization issue

Let \(V(Q,x;\tau,m)=\sum_k Q^{m\cdot k}\mathcal I(k)\), with the
original grading and zero extension. The exact finite reindexing
dictionary of [J] is
\[
 S_i\longmapsto M_i,\qquad X_i\longmapsto\mathsf E_i,\qquad
 M_i f(m)=Q^{-m_i}f(m),\qquad
 M_i\mathsf E_j=Q^{\delta_{ij}}\mathsf E_jM_i .
 \tag{24}
\]
A translated grading coefficient is still finite. In particular
its literal factor \(\tau^{T(v)}\) is already in (17); no new
grading factor is inserted in (24).

Consequently (19) gives the boundary-exact full-clock equation
\[
 \boxed{\quad
 \left[
  \mathcal B_{j,v}(Q,Y,\tau,\mathsf E)\,\mathsf T^jM^v
            -\mathcal A_{j,v}(Q,Y,\tau,\mathsf E)
 \right]V=0 .
 \quad}
 \tag{25}
\]
The coefficient must not be moved through \(M^v\) without its
\(Q\)-commutation. Expanding in \(h=\log Q\), the rational
grading completion in [J] transports this identity to the actual
\(\mathscr W_m(h,Y)\) at grading one, coefficientwise and then
meromorphically in \(Y\). Its rescaled Borel dictionary is exactly
[J, (10)--(15)], with all clocks, the original external shift,
and its primitive constants retained.

The improvement over the general boundary-safe construction of
[J] is precise. For these unreduced coefficients one does not
need an additional common multiplier \(\Theta_v\).
The required zeros have already been distributed between the
two coefficient sides in (21) and (23). This uses both the
specific support lemma and the literal inverse factorials.
It is not a statement about arbitrary proper hypergeometric sums.

It also does not authorize reducing the displayed fraction.
If \(\mathcal A=G A_{\rm red}\) and
\(\mathcal B=G B_{\rm red}\), (19) asserts
\[
                 G(B_{\rm red}\mathsf T^jS^v-A_{\rm red})
                                      \mathcal I=0,
 \tag{26}
\]
and the zeros of \(G\) on boundary strata need not be units.
One cannot delete \(G\) from this source equation merely because
it cancels in a generic ratio. The same warning applies to
analytic division of natural factors in (25).

The highest-vacuum equations and forced linear-face equations
of [J] remain valid and useful. An unreduced ratio can still
degenerate to \(0=0\) on a forced face. No non-forced clock factor
is declared invertible, and no finite-dimensional E/F closure,
marked moving minor, or multiplicative clock amplitude follows
from (25) alone.

## 6. Complete proof directs

| Label | Complete proof source | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| J | notes/research_highest_cut_joint_clock_equations.md | a2cf72961c37d6c96625bf8ff85ab94776ef328fcacc1f78c82bb9b9a7f16e2d |

F supplies the literal signed source entries, original framing,
and pathwise parity. J supplies its fixed integral matching
lattice, zero extension, clock ordering, and coefficientwise
completion adapter. The reduced support, all unreduced products,
and every boundary case are proved above.

The complete directs and the entire final were read, and all
used implications checked. Only written mathematics, text reads
and hash checks were used. Frozen notes and public manuscripts
are unchanged.
