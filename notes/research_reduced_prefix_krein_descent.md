# Krein adjoints descend through the actual prefix reduction

Written research proof, 23 November 2026.

The actual triangular prefix change is an isometry for the fixed
physical tensor Krein form on positive real meridians. Its
constant-coefficient reduction preserves adjoints. Consequently the
literal reduced braid matrices, including their boundary Euler
generator and full Cartan scalar, preserve the same tensor form on
the remaining heads. This is an algebraic descent through a
star-stable nilpotent ideal, not restriction of the form to the
first-head vacuum, which is isotropic.

All statements are at the actual fixed quantum root, including even
and composite levels. The form is indefinite. No marked scalar lower
bound or identification of geometric eigenline contributions follows.

## 1. Actual matrices and the fixed tensor form

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad F_n=(Q;Q)_n\quad(0\le n<N).
 \tag{1}
\]
Keep this quantum parameter fixed. The common meridian is
\(M>0\), with \(x=-M/q\) and the real branch of \(\Log M\).
Use the original balanced occupation basis \(|a\rangle\),
\(0\le a\le d\), and the literal operators of [R]:
\[
 K|a\rangle=xQ^{-a}|a\rangle,\qquad
 F|a\rangle=(1-Q^{a+1})|a+1\rangle,\qquad
 L|a\rangle=|a-1\rangle.
 \tag{2}
\]
The raising arrow at \(a=d\) and the lowering arrow at \(a=0\)
are zero. No cyclic completion is made. Put
\[
 H_N=q^{-1}Z^{-1}R_d,\quad Z|a\rangle=Q^a|a\rangle,
 \quad R_d|a\rangle=|d-a\rangle,\quad
 \mathscr H_b=H_N^{\otimes b}.
 \tag{3}
\]
Thus \(H_N|a\rangle=qQ^a|d-a\rangle\),
\(H_N^\dagger=H_N\), and \(H_N^2=I\). For an operator on
\(b\) heads write \(A^{\sharp_b}=\mathscr H_bA^\dagger\mathscr H_b\).
When the number of heads is clear the subscript is omitted.

The direct head identities are
\[
 K^\sharp=K,\qquad F^\sharp=Q^{-1}F,\qquad
 L^\sharp=QL,\qquad \bar x=Qx .
 \tag{4}
\]
The first two are [H, (4)]. For the third, on input \(a\ge1\),
the coefficient of \(H_NL^\dagger H_N\) is
\(q^2Q^{a+d-a+1}=Q\); at \(a=0\) the actual top zero
of \(L^\dagger\) gives zero. Thus both endpoints satisfy (4).

On \(m\ge2\) ordered heads let \(r=m-1\) and retain the actual
remaining coproduct
\[
 F_{\rm r}=F_2+K_2^{-1}F_3+\cdots+
                   K_2^{-1}\cdots K_{m-1}^{-1}F_m,
 \quad F_\Sigma=F_1+K_1^{-1}F_{\rm r}.
 \tag{5}
\]
Distinct head factors commute. Consequently (4) gives
\(F_{\rm r}^{\sharp_r}=Q^{-1}F_{\rm r}\) and
\(F_\Sigma^{\sharp_m}=Q^{-1}F_\Sigma\), with every original
finite arrow retained.

## 2. The prefix itself is an isometry

[R, (2)] specifies the actual prefix and its transport:
\[
 Y=x^{-1}L_1F_{\rm r},\qquad
 S_m=e_Q(Y):=\sum_{n=0}^d\frac{Y^n}{F_n},\qquad
 S_m^{-1}F_\Sigma S_m=F_1.
 \tag{6}
\]
For one head use \(S_1=I\). Since \(L_1^N=0\), \(Y^N=0\).
The transport identity in (6) is an identity of finite Laurent
matrices in \(M\); its equality near one therefore holds at every
nonzero \(M\), in particular on the positive real axis.
The factors in its adjoint commute across the two tensor groups;
(4)--(5) therefore imply exactly
\[
 Y^{\sharp_m}=\bar x^{-1}(Q^{-1}F_{\rm r})(QL_1)
                                      =Q^{-1}Y.
 \tag{7}
\]
Use the finite factorial conjugation and inverse from [H, (7)]:
\[
 \overline{F_n}=(-1)^nQ^{-n(n+1)/2}F_n,\qquad
 P_Q(Y)=\sum_{n=0}^d
          \frac{(-1)^nQ^{n(n-1)/2}Y^n}{F_n}
                                      =e_Q(Y)^{-1}.
 \tag{8}
\]
The inverse identity follows below degree \(N\) from the finite
\(Q\)-binomial formula; higher powers vanish. In particular no
denominator \(F_N\) occurs. Combining (7)--(8) gives
\[
 \boxed{\quad S_m^{\sharp_m}=P_Q(Y)=S_m^{-1},\qquad
                  S_m^\dagger\mathscr H_mS_m=\mathscr H_m .\quad}
 \tag{9}
\]
There is no meridian-dependent metric or omitted diagonal scalar.

## 3. Constant coefficients preserve adjoints

Let \(\mathcal C_\Sigma\) be the full matrix commutant of
\(F_\Sigma\), at a fixed positive real \(M\). It is stable under
\(\sharp_m\), since \(F_\Sigma^\sharp=Q^{-1}F_\Sigma\).
After conjugating by \(S_m\), its elements have unique expansions
\[
 \widetilde W=S_m^{-1}WS_m
            =\sum_{n=0}^d F_1^n\otimes B_n(W).
 \tag{10}
\]
Indeed \(F_1\) is one nilpotent Jordan block: its nonzero
arrows below the top are units. The column on \(|0\rangle\)
determines all columns by commutation with \(F_1\), proving (10).
This is the same commutant calculation used in [R, (3)].

Define \(\mathcal B_m(W)=B_0(W)\). This is the actual prefix
map, not a different compression: for
\(i_0v=|0\rangle\otimes v\), [R] gives
\(S_mi_0=i_0\) and
\(B_0=p_0S_m^{-1}Wi_0\). Positive \(F_1\)-degree cannot
contribute to a constant coefficient, so \(\mathcal B_m\)
is a unital algebra homomorphism. Moreover (9) yields
\[
 S_m^{-1}W^{\sharp_m}S_m=\widetilde W^{\sharp_m}
       =\sum_{n=0}^dQ^{-n}F_1^n\otimes B_n(W)^{\sharp_r}.
 \tag{11}
\]
Taking its constant coefficient proves the exact descent
\[
 \boxed{\quad
 \mathcal B_m(W^{\sharp_m})
             =\mathcal B_m(W)^{\sharp_r}.
 \quad}
 \tag{12}
\]
Equivalently, the ideal of positive \(F_1\)-degree in (10)
is star-stable and nilpotent, and its quotient carries the
displayed tensor adjoint on the entire remaining matrix algebra.
This calculation retains all coefficient matrices \(B_n\)
before passing to that specified quotient.

In particular, if an invertible actual total intertwiner satisfies
\(W^{\sharp_m}W=I\), then
\[
 \boxed{\quad
 B(W)^\dagger\mathscr H_rB(W)=\mathscr H_r,\qquad
 B(W)^{-1}=\mathscr H_rB(W)^\dagger\mathscr H_r .\quad}
 \tag{13}
\]
Here and below \(B(W)=\mathcal B_m(W)\).
This applies to the full original common-meridian signed braid
words of [H], including overlapping adjacent crossings.

The descent is not restriction to the vacuum section:
\[
 i_0^\dagger S_m^\dagger\mathscr H_mS_mi_0=0,
 \qquad
 i_0^\dagger S_m^\dagger\mathscr H_mS_mi_d
                                      =q^{-1}\mathscr H_r,
 \quad i_dv=|d\rangle\otimes v.
 \tag{14}
\]
These follow from (9) and the first-head anti-diagonal in (3).
Thus the vacuum is isotropic, while its pairing with the opposite
end is nondegenerate. The algebra quotient proof, rather than a
nonexistent positive vacuum restriction, gives (13).

## 4. The literal reduced boundary generator checks its scalar

For the original checked crossing [R, (7),(12)] gives
\[
 B(R_i)=R_{i-1}\ (i\ge2),\qquad
 B(R_1)=\kappa(M)S_rD_{\rm red},\qquad
 B(R_1^{-1})=\kappa(M)^{-1}D_{\rm red}^{-1}S_r^{-1},
 \tag{15}
\]
where on the first remaining head
\[
 D_{\rm red}|a\rangle
      =\delta_a|a\rangle,\quad
 \delta_a=(-1)^aq^{a(a+1)}M^{-2a},\quad
 \alpha(M)=d+\frac{N}{\pi i}\Log M,\quad
 \kappa(M)=q^{\alpha(M)^2/2},\quad |\kappa(M)|=M^d.
 \tag{16}
\]
The last modulus follows by substituting real \(\Log M\)
in the displayed unrolled exponent. For the diagonal,
\[
 \overline{\delta_{d-a}}\delta_a=M^{-2d},\qquad
 D_{\rm red}^{\sharp_r}D_{\rm red}=M^{-2d}I.
 \tag{17}
\]
In fact its phase is
\((-1)^dq^{(2a-d)(d+1)}=1\). Equations (9),(16)--(17)
prove (13) directly for the boundary generator. Dropping
\(\kappa\) would leave the incorrect factor \(M^{-2d}\).
Internal generators use [H]'s full physical crossing identity.
The actual negative generators have the inverse order in (15),
so products of arbitrary signs preserve \(\mathscr H_r\).

The zero-framed normalized boundary generator is instead
\(x^dS_rD_{\rm red}\), as in [R, (23)]. It is also an
isometry because \(|x|=M\). Equivalently its retained twist
\(\kappa x^{-d}\) has modulus one on positive real meridians.
No external modified-dimension or other prescribed peripheral
factor is thereby declared an isometry.

## 5. Meridian germs and the original pointed source

Fix \(M_0>0\) and put \(M=M_0e^u\) on its continued logarithmic
branch. Holomorphic polarization of (13), as in [H], gives for
the full actual reduced braid germ
\[
 B^\natural(u)\mathscr H_rB(u)=\mathscr H_r,
 \qquad B^\natural(u)=\overline{B(\bar u)}^{\mathsf T}.
 \tag{18}
\]
Thus all fixed-order meridian Wronskians follow together:
\[
 \sum_{j=0}^n\binom nj
 B^{(j)}(0)^\dagger\mathscr H_rB^{(n-j)}(0)
                         =\mathbf1_{n=0}\mathscr H_r.
 \tag{19}
\]
This includes the meridian dependence of the prefix itself.
There is no differentiation in \(q\).

In particular the original highest-cut pivotal observation stays
exactly [R, (14)]. Write \(K_{\rm r}(M)=M^rK_0\),
\(\varepsilon=(-1)^{(N+1)r}\), and
\(\mathcal D_N(z)=(z^N-z^{-N})/(z-z^{-1})\) with its
Laurent-polynomial continuation. Then
\[
 \Phi_0(W(M))=
 \frac{\mathcal D_N(M)}{\varepsilon(M^{mN}-M^{-mN})}
 \operatorname{Tr}\bigl[(M^mK_0-M^{-m}K_0^{-1})B(M)\bigr].
 \tag{20}
\]
It is read meromorphically with the original removable continuation.
For an analytic actual intertwiner, \(\mathcal D_N(1)=N\)
forces \(\operatorname{Tr}((K_0-K_0^{-1})B(1))=0\).
Differentiating its numerator and denominator before specialization
therefore gives the unchanged first-meridian-jet row
\[
 \Phi_0(W(1))=
 \frac{\operatorname{Tr}((K_0+K_0^{-1})B(1))}{2\varepsilon}
 +\frac{\operatorname{Tr}((K_0-K_0^{-1})B'(1))}{2\varepsilon m}.
 \tag{21}
\]
Here the prime is \(\partial_M\), and the whole prefix dependence
is included. External marking, framing and peripheral lines remain
in their original positions. The source is not replaced by an
\(\mathscr H_r\)-norm, an adjoint vacuum, or an ordinary trace.

The same form also respects this actual source functional. At
positive real \(M\), put
\(C_N(M)=\mathcal D_N(M)\mathcal D_N(MK_{\rm r}(M))^{-1}\).
Since \(K_{\rm r}^\sharp=K_{\rm r}\) and \(\mathcal D_N\)
has real Laurent coefficients, \(C_N^\sharp=C_N\) wherever
defined. For every remaining matrix \(B\), cyclic trace then gives
\[
 \overline{\operatorname{Tr}(C_NB)}
        =\operatorname{Tr}(C_NB^{\sharp_r}),\qquad
 \overline{\Phi_0(W(M))}=\Phi_0(W(M)^{-1})
       \quad(W^{\sharp_m}W=I).
 \tag{22}
\]
The second equality uses the actual algebra map and (13).
These identities continue as polarized meromorphic germs. For
analytic original intertwiner families their removable values at
one retain the complete first-jet row (21). An additional external
scalar carries its own complex conjugate; it is not assumed unit.
The functional in (22) is not asserted positive.

## 6. Scope and complete sources

The new operation is the actual prefix star descent (9)--(13).
It gives one common nondegenerate form for the complete reduced
braid representation and its meridian germs. It does not remove
any remaining head, root Jordan direction, or source coefficient.
The physical dimension is still \(N^{m-1}\). No positive metric,
geometric packet estimate, nonzero marked closing, comparison of
off-circle geometric eigenlines, or general volume lower bound is
asserted. Moving-\(q\) normal jets retain their separate original
prefix adapters and are outside this fixed-root meridian proof.

Both complete direct texts were read at the matching pins:

| Source | SHA-256 |
|---|---|
| [R: Actual reduced braid source](research_actual_reduced_braid_source.md), 330 lines | `9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243` |
| [H: Real-meridian physical Krein transport](research_real_meridian_krein_transport.md), 310 lines | `caf18090cb75a0527ffccdf4a3217fe422876d683271eda8e3e6d591259e92dc` |

The complete [physical tensor-form proof](research_physical_tensor_krein_crossing_form.md),
286 lines, SHA-256 `610b5ac7d889429163ec230e9d644d174d38382733dbad57826fce66cec8e348`,
was read for coverage. The current proof uses the generic-meridian
head identities and full crossing of [H], rather than its complete-only
flag-frame congruence. Only written mathematics and text/hash operations
were used; earlier final files remain unchanged.
